// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.ApplicationModel.Payments.h>

namespace py::proj::Windows::ApplicationModel::Payments
{}

namespace py::impl::Windows::ApplicationModel::Payments
{
    struct PaymentRequestChangedHandler
    {
        static winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };
                py::pyobj_handle py_param1{ py::convert(param1) };

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::ApplicationModel::Payments
{
    using PaymentAddress = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentAddress>;
    using PaymentCanMakePaymentResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentCanMakePaymentResult>;
    using PaymentCurrencyAmount = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentCurrencyAmount>;
    using PaymentDetails = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentDetails>;
    using PaymentDetailsModifier = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentDetailsModifier>;
    using PaymentItem = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentItem>;
    using PaymentMediator = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentMediator>;
    using PaymentMerchantInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentMerchantInfo>;
    using PaymentMethodData = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentMethodData>;
    using PaymentOptions = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentOptions>;
    using PaymentRequest = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentRequest>;
    using PaymentRequestChangedArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedArgs>;
    using PaymentRequestChangedResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedResult>;
    using PaymentRequestSubmitResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentRequestSubmitResult>;
    using PaymentResponse = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentResponse>;
    using PaymentShippingOption = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentShippingOption>;
    using PaymentToken = py::winrt_wrapper<winrt::Windows::ApplicationModel::Payments::PaymentToken>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentAddress>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentCanMakePaymentResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentCurrencyAmount>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentDetailsModifier>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentItem>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentMediator>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentMerchantInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentMethodData>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentOptions>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentRequestSubmitResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentResponse>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentShippingOption>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Payments::PaymentToken>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::ApplicationModel::Payments::PaymentRequestChangedHandler>
    {
        using type = py::impl::Windows::ApplicationModel::Payments::PaymentRequestChangedHandler;
    };

}
