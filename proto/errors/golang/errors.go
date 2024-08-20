package errors

import (
	"fmt"

	"google.golang.org/genproto/googleapis/rpc/errdetails"
	spb "google.golang.org/genproto/googleapis/rpc/status"
	"google.golang.org/grpc/codes"
	gst "google.golang.org/grpc/status"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/anypb"
)

// Error defines the error interface
type Error interface {
	// Code returns the error code
	Code() int
	// Name returns the name of the error
	Name() string
	// Message returns the message of this error
	Message() string
	// URI returns the uri of this error
	URI() string
	// New creates a new error from this error with new message
	New(message interface{}, args ...interface{}) Error
	// NewWithURI creates a new error from this error with new message and uri
	NewWithURI(message interface{}, uri string) Error
	// NewWithDetails creates a new error from this error with details
	NewWithDetails(details ...interface{}) Error
	// Status returns the grpc status
	Status() (*spb.Status, error)
	// GRPC returns the error for grpc
	GRPC() error
	// Error return the error string
	Error() string
}

// New creates a new Error
func New(code int, name, message, uri string, details ...interface{}) Error {
	return &_error{code, name, message, uri, details}
}

// NewFromError creates a new Error from error
func NewFromError(err error) Error {
	// Try `Error` interface
	e, ok := err.(Error)
	if ok {
		return e
	}

	// Try decode by grpc error
	s, ok := gst.FromError(err)
	if ok {
		var details []interface{}
		for _, v := range s.Proto().GetDetails() {
			details = append(details, v)
		}
		return New(int(s.Code()), "", s.Message(), "", details...)
	}
	// Create a new internal error
	return ErrInternal.New(err.Error())
}

// _error implements Error interface
type _error struct {
	code    int
	name    string
	message string
	uri     string
	details []interface{}
}

// Code returns the error code
func (e *_error) Code() int {
	return e.code
}

// Name returns the name of the error
func (e *_error) Name() string {
	return e.name
}

// Message returns the message of this error
func (e *_error) Message() string {
	return e.message
}

// URI returns the uri of this error
func (e *_error) URI() string {
	return e.uri
}

// New creates a new error from this error with new message
func (e *_error) New(message interface{}, args ...interface{}) Error {
	_e := e.clone()
	if message != nil {
		if len(args) > 0 {
			_e.message = fmt.Sprintf(fmt.Sprintf("%v", message), args...)
		} else {
			_e.message = fmt.Sprintf("%v", message)
		}
	}
	return _e
}

// NewWithURI creates a new error from this error with new message and uri
func (e *_error) NewWithURI(message interface{}, uri string) Error {
	_e := e.clone()
	if message != nil {
		_e.message = fmt.Sprintf("%v", message)
	}
	_e.uri = uri
	return _e
}

// NewWithDetails creates a new error from this error with details
func (e *_error) NewWithDetails(details ...interface{}) Error {
	_e := e.clone()
	_e.details = append(_e.details, details...)
	return _e
}

// Status returns the grpc status
func (e *_error) Status() (*spb.Status, error) {
	if e == nil {
		return nil, nil
	}
	var status spb.Status
	status.Code = int32(e.code)
	status.Message = e.message
	if e.message != "" && e.uri != "" {
		any, err := anypb.New(&errdetails.Help{
			Links: []*errdetails.Help_Link{
				{
					Description: e.message,
					Url:         e.uri,
				},
			},
		})
		if err != nil {
			return nil, err
		}
		status.Details = append(status.Details, any)
	}
	for _, detail := range e.details {
		if detail != nil {
			if pbMsg, ok := detail.(proto.Message); ok {
				pbAny, err := anypb.New(pbMsg)
				if err != nil {
					return nil, err
				}
				status.Details = append(status.Details, pbAny)
			} else if pbAny, ok := detail.(*anypb.Any); ok {
				status.Details = append(status.Details, pbAny)
			} else {
				// Ignore this detail
			}
		}
	}
	return &status, nil
}

// GRPC returns the error for grpc
func (e *_error) GRPC() error {
	status, err := e.Status()
	if err != nil {
		return gst.New(codes.Internal, fmt.Sprintf("Failed to marshal error detail: %v", err)).Err()
	}
	if status == nil {
		return nil
	}
	return gst.FromProto(status).Err()
}

// Error
func (e *_error) Error() string {
	return e.GRPC().Error()
}

func (e *_error) clone() *_error {
	if e == nil {
		return new(_error)
	}
	_e := *e
	if _e.details != nil {
		// Copy slice
		_details := make([]interface{}, len(e.details))
		copy(_details, e.details)
		_e.details = _details
	}
	return &_e
}

// The predefined errors
var (
	// 无错误
	ErrOK Error
	// 已取消
	ErrCancelled Error
	// 未知错误（类型）
	ErrUnknown Error
	// 无效的参数
	ErrInvalidArgument Error
	// 超时
	ErrDeadlineExceeded Error
	// 未找到
	ErrNotFound Error
	// 已经存在
	ErrAlreadyExists Error
	// 访问被拒绝
	ErrPermissionDenied Error
	// 资源耗尽
	ErrResourceExhausted Error
	// 前置条件不满足
	ErrFailedPrecondition Error
	// 已终止
	ErrAborted Error
	// 超出范围
	ErrOutOfRange Error
	// 未实现
	ErrUnimplemented Error
	// 内部错误
	ErrInternal Error
	// 数据库错误
	ErrDatabase Error
	// 不可能
	ErrUnavailable Error
	// 数据丢失
	ErrDataLoss Error
	// 未认证
	ErrUnauthenticated Error
	// 重定向
	ErrRedirect Error
)

func init() {
	// Initialize errors
	ErrOK = New(int(Code_OK), Code_name[int32(Code_OK)], "OK", "")
	ErrCancelled = New(int(Code_Cancelled), Code_name[int32(Code_Cancelled)], "Cancelled", "")
	ErrUnknown = New(int(Code_Unknown), Code_name[int32(Code_Unknown)], "Unknown", "")
	ErrInvalidArgument = New(int(Code_InvalidArgument), Code_name[int32(Code_InvalidArgument)], "InvalidArgument", "")
	ErrDeadlineExceeded = New(int(Code_DeadlineExceeded), Code_name[int32(Code_DeadlineExceeded)], "DeadlineExceeded", "")
	ErrNotFound = New(int(Code_NotFound), Code_name[int32(Code_NotFound)], "NotFound", "")
	ErrAlreadyExists = New(int(Code_AlreadyExists), Code_name[int32(Code_AlreadyExists)], "AlreadyExists", "")
	ErrPermissionDenied = New(int(Code_PermissionDenied), Code_name[int32(Code_PermissionDenied)], "PermissionDenied", "")
	ErrResourceExhausted = New(int(Code_ResourceExhausted), Code_name[int32(Code_ResourceExhausted)], "ResourceExhausted", "")
	ErrFailedPrecondition = New(int(Code_FailedPrecondition), Code_name[int32(Code_FailedPrecondition)], "FailedPrecondition", "")
	ErrAborted = New(int(Code_Aborted), Code_name[int32(Code_Aborted)], "Aborted", "")
	ErrOutOfRange = New(int(Code_OutOfRange), Code_name[int32(Code_OutOfRange)], "OutOfRange", "")
	ErrUnimplemented = New(int(Code_Unimplemented), Code_name[int32(Code_Unimplemented)], "Unimplemented", "")
	ErrInternal = New(int(Code_Internal), Code_name[int32(Code_Internal)], "Internal", "")
	ErrDatabase = New(int(Code_Internal), Code_name[int32(Code_Internal)], "Internal Database Error", "")
	ErrUnavailable = New(int(Code_Unavailable), Code_name[int32(Code_Unavailable)], "Unavailable", "")
	ErrDataLoss = New(int(Code_DataLoss), Code_name[int32(Code_DataLoss)], "DetaLoss", "")
	ErrUnauthenticated = New(int(Code_Unauthenticated), Code_name[int32(Code_Unauthenticated)], "Unauthenticated", "")
	ErrRedirect = New(int(Code_Redirect), Code_name[int32(Code_Redirect)], "Redirect", "")
}
