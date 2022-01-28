// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.ApplicationModel.Search.h>

namespace py::proj::Windows::ApplicationModel::Search
{}

namespace py::impl::Windows::ApplicationModel::Search
{}

namespace py::wrapper::Windows::ApplicationModel::Search
{
    using LocalContentSuggestionSettings = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::LocalContentSuggestionSettings>;
    using SearchPaneQueryLinguisticDetails = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::SearchPaneQueryLinguisticDetails>;
    using SearchQueryLinguisticDetails = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::SearchQueryLinguisticDetails>;
    using SearchSuggestionCollection = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::SearchSuggestionCollection>;
    using SearchSuggestionsRequest = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::SearchSuggestionsRequest>;
    using SearchSuggestionsRequestDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::Search::SearchSuggestionsRequestDeferral>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::LocalContentSuggestionSettings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::SearchPaneQueryLinguisticDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::SearchQueryLinguisticDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::SearchSuggestionCollection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::SearchSuggestionsRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Search::SearchSuggestionsRequestDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
