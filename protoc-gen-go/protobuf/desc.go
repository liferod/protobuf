package protobuf

import (
	"errors"
	"fmt"
	"net/http"
	"reflect"

	"github.com/liferod/protobuf/protoc-gen-go/protobuf/options"
	googleapi "google.golang.org/genproto/googleapis/api/annotations"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protodesc"
	"google.golang.org/protobuf/reflect/protoreflect"
	descriptor "google.golang.org/protobuf/types/descriptorpb"
)

// ServiceDesc The service desc
type ServiceDesc struct {
	methods    map[string]*MethodDesc // The key is method name which is the one defined in proto file
	descriptor *descriptor.ServiceDescriptorProto
	pkg        string
}

// NewServiceDesc Create new ServiceDesc from service descriptor
func NewServiceDesc(d *descriptor.ServiceDescriptorProto, pkg string) (*ServiceDesc, error) {
	service := &ServiceDesc{make(map[string]*MethodDesc), d, pkg}

	for _, md := range d.Method {
		methodDesc, err := NewMethodDesc(md, service, pkg)
		if err != nil {
			return nil, fmt.Errorf("Failed to get method description of [%s] error: %s", md.GetName(), err)
		}
		service.methods[md.GetName()] = methodDesc
	}
	return service, nil
}

// Methods returns the internal method map
func (desc *ServiceDesc) Methods() map[string]*MethodDesc {
	return desc.methods
}

// Descriptor returns the descriptor
func (desc *ServiceDesc) Descriptor() *descriptor.ServiceDescriptorProto {
	return desc.descriptor
}

// Package returns the package
func (desc *ServiceDesc) Package() string {
	return desc.pkg
}

// GetFullname returns the service fullname
func (desc *ServiceDesc) GetFullname() string {
	return fmt.Sprintf("/%s.%s", desc.pkg, desc.descriptor.GetName())
}

type HttpRule struct {
	Method     string
	Path       string
	ExtraRules []*HttpRule
}

// NewHttpRule convert http rules to verb actions
func NewHttpRule(r *googleapi.HttpRule) (*HttpRule, error) {
	if r == nil {
		return nil, nil
	}

	rule := HttpRule{}
	switch v := r.Pattern.(type) {
	case *googleapi.HttpRule_Get:
		rule.Method = http.MethodGet
		rule.Path = v.Get
	case *googleapi.HttpRule_Post:
		rule.Method = http.MethodPost
		rule.Path = v.Post
	case *googleapi.HttpRule_Put:
		rule.Method = http.MethodPut
		rule.Path = v.Put
	case *googleapi.HttpRule_Patch:
		rule.Method = http.MethodPatch
		rule.Path = v.Patch
	case *googleapi.HttpRule_Delete:
		rule.Method = http.MethodDelete
		rule.Path = v.Delete
	case *googleapi.HttpRule_Custom:
		rule.Method = "CUSTOM"
		rule.Path = v.Custom.Path
	}

	for _, subR := range r.GetAdditionalBindings() {
		if subRule, err := NewHttpRule(subR); err != nil {
			return nil, err
		} else {
			rule.ExtraRules = append(rule.ExtraRules, subRule)
		}
	}
	return &rule, nil
}

// MethodDesc The method description
type MethodDesc struct {
	authRule   *options.AuthRule
	httpRule   *HttpRule
	descriptor *descriptor.MethodDescriptorProto
	service    *ServiceDesc
	pkg        string
}

// NewMethodDesc Create new MethodDesc from method descriptor
func NewMethodDesc(d *descriptor.MethodDescriptorProto, service *ServiceDesc, pkg string) (*MethodDesc, error) {
	var (
		authRule *options.AuthRule
		httpRule *HttpRule
	)
	// Get auth rule
	if d.GetOptions() != nil {
		if authExtension := proto.GetExtension(d.GetOptions(), E_Auth); authExtension != nil {
			if rule, ok := authExtension.(*options.AuthRule); !ok {
				return nil, errors.New("Failed to convert auth extension to AuthRule")
			} else if rule != nil && rule.Level != options.AuthLevel_NoAuth {
				authRule = rule
			}
		}
		if httpExtension := proto.GetExtension(d.GetOptions(), googleapi.E_Http); httpExtension != nil {
			if googleapiHttpRule, ok := httpExtension.(*googleapi.HttpRule); !ok {
				return nil, errors.New("Failed to convert googleapi http extension")
			} else if rule, err := NewHttpRule(googleapiHttpRule); err != nil {
				return nil, err
			} else if rule != nil {
				httpRule = rule
			}
		}
		//if authRule != nil && authRule.Verb == 0 && httpRule != nil {
		//	switch httpRule.Method {
		//	case http.MethodGet, http.MethodHead:
		//		authRule.Verb = options.ScopeVerb_GET
		//	case http.MethodPost:
		//		authRule.Verb = options.ScopeVerb_CREATE
		//	case http.MethodPut, http.MethodPatch:
		//		authRule.Verb = options.ScopeVerb_UPDATE
		//	case http.MethodDelete:
		//		authRule.Verb = options.ScopeVerb_DELETE
		//	default:
		//		return nil, errors.New("Failed to auto infer api verb")
		//	}
		//}
	}
	return &MethodDesc{authRule, httpRule, d, service, pkg}, nil
}

// Descriptor returns the descriptor
func (desc *MethodDesc) Descriptor() *descriptor.MethodDescriptorProto {
	return desc.descriptor
}

// Service returns the service
func (desc *MethodDesc) Service() *ServiceDesc {
	return desc.service
}

// Package returns the package
func (desc *MethodDesc) Package() string {
	return desc.pkg
}

// GetFullname Get the fullname
func (desc *MethodDesc) GetFullname() string {
	return fmt.Sprintf("%s/%s", desc.service.GetFullname(), desc.descriptor.GetName())
}

func (desc *MethodDesc) AuthRule() *options.AuthRule {
	return desc.authRule
}

func (desc *MethodDesc) HttpRule() *HttpRule {
	return desc.httpRule
}

// EnumDesc defines the enum data type definition
type EnumDesc struct {
	values map[int32]*EnumValueDesc
}

// GetValue gets the value desc by value
func (desc *EnumDesc) GetValue(value int32) *EnumValueDesc {
	return desc.values[value]
}

// Values returns the internal values
func (desc *EnumDesc) Values() map[int32]*EnumValueDesc {
	return desc.values
}

// EnumValueDesc defines the enum value data type definition
type EnumValueDesc struct {
	name  string // The protobuf name of this enum value
	value int32  // The protobuf value of this enum value
	text  string // The extension text value
}

// Name returns the name
func (desc *EnumValueDesc) Name() string {
	return desc.name
}

// Value returns the value
func (desc *EnumValueDesc) Value() int32 {
	return desc.value
}

// Text returns the text
func (desc *EnumValueDesc) Text() string {
	return desc.text
}

//
// Helper methods used to extract desc from protobuf definitions
//

// LoadFileDescriptors loads a file descriptor from bytes
// func LoadFileDescriptors(gzs ...[]byte) ([]*descriptor.FileDescriptorProto, error) {
// 	var descs []*descriptor.FileDescriptorProto
// 	for _, gz := range gzs {
// 		r, err := gzip.NewReader(bytes.NewReader(gz))
// 		if err != nil {
// 			return nil, fmt.Errorf("Failed to open gzip reader: %v", err)
// 		}
// 		defer r.Close()
// 		// Read gzip content
// 		b, err := ioutil.ReadAll(r)
// 		if err != nil {
// 			return nil, fmt.Errorf("Failed to uncompress descriptor: %v", err)
// 		}
// 		// Unmarshal file descriptor
// 		fileDescriptor := new(descriptor.FileDescriptorProto)
// 		if err := proto.Unmarshal(b, fileDescriptor); err != nil {
// 			return nil, fmt.Errorf("Malformed FileDescriptorProto: %v", err)
// 		}
// 		// Add
// 		descs = append(descs, fileDescriptor)
// 	}
// 	return descs, nil
// }

func LoadFileDescriptors(fs ...protoreflect.FileDescriptor) ([]*descriptor.FileDescriptorProto, error) {
	var descs []*descriptor.FileDescriptorProto
	for _, f := range fs {
		descs = append(descs, protodesc.ToFileDescriptorProto(f))
	}
	return descs, nil
}

// LoadServiceDescs loads service desc from file descriptors
func LoadServiceDescs(fileDescriptors ...*descriptor.FileDescriptorProto) ([]*ServiceDesc, error) {
	var descs []*ServiceDesc
	for _, fileDescriptor := range fileDescriptors {
		for _, serviceDescriptor := range fileDescriptor.Service {
			desc, err := NewServiceDesc(serviceDescriptor, fileDescriptor.GetPackage())
			if err != nil {
				return nil, fmt.Errorf("Failed to create new service description of [%s] error: %s", serviceDescriptor.GetName(), err)
			}
			descs = append(descs, desc)
		}
	}
	return descs, nil
}

// LoadEnumDescs loads enum desc from file descriptors
func LoadEnumDescs(fileDescriptors ...*descriptor.FileDescriptorProto) ([]*EnumDesc, error) {
	var descs []*EnumDesc
	for _, fileDescriptor := range fileDescriptors {
		for _, enumDescriptor := range fileDescriptor.GetEnumType() {
			var desc EnumDesc
			desc.values = make(map[int32]*EnumValueDesc)
			for _, enumValueDescriptor := range enumDescriptor.Value {
				var valueDesc EnumValueDesc
				valueDesc.name = enumValueDescriptor.GetName()
				valueDesc.value = enumValueDescriptor.GetNumber()
				// Try get text
				if enumValueDescriptor.GetOptions() != nil {
					if extension := proto.GetExtension(enumValueDescriptor.GetOptions(), E_Text); extension != nil {
						if text, ok := extension.(string); !ok {
							return nil, fmt.Errorf("Failed to convert extension to text, type: %v", reflect.TypeOf(extension))
						} else {
							valueDesc.text = text
						}
					}
				}
				// Add
				desc.values[valueDesc.value] = &valueDesc
			}
			// Add
			descs = append(descs, &desc)
		}
	}
	return descs, nil
}

// MergeServiceDescs merges service desc
func MergeServiceDescs(descs ...[]*ServiceDesc) map[string]*ServiceDesc {
	mergedDescs := make(map[string]*ServiceDesc)
	for _, desc := range descs {
		for _, value := range desc {
			mergedDescs[value.GetFullname()] = value
		}
	}
	return mergedDescs
}
