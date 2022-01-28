# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Data.Text")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.ui.text.core
except Exception:
    pass

class AlternateNormalizationFormat(enum.IntEnum):
    NOT_NORMALIZED = 0
    NUMBER = 1
    CURRENCY = 3
    DATE = 4
    TIME = 5

class TextPredictionOptions(enum.IntFlag):
    NONE = 0
    PREDICTIONS = 0x1
    CORRECTIONS = 0x2

class UnicodeGeneralCategory(enum.IntEnum):
    UPPERCASE_LETTER = 0
    LOWERCASE_LETTER = 1
    TITLECASE_LETTER = 2
    MODIFIER_LETTER = 3
    OTHER_LETTER = 4
    NONSPACING_MARK = 5
    SPACING_COMBINING_MARK = 6
    ENCLOSING_MARK = 7
    DECIMAL_DIGIT_NUMBER = 8
    LETTER_NUMBER = 9
    OTHER_NUMBER = 10
    SPACE_SEPARATOR = 11
    LINE_SEPARATOR = 12
    PARAGRAPH_SEPARATOR = 13
    CONTROL = 14
    FORMAT = 15
    SURROGATE = 16
    PRIVATE_USE = 17
    CONNECTOR_PUNCTUATION = 18
    DASH_PUNCTUATION = 19
    OPEN_PUNCTUATION = 20
    CLOSE_PUNCTUATION = 21
    INITIAL_QUOTE_PUNCTUATION = 22
    FINAL_QUOTE_PUNCTUATION = 23
    OTHER_PUNCTUATION = 24
    MATH_SYMBOL = 25
    CURRENCY_SYMBOL = 26
    MODIFIER_SYMBOL = 27
    OTHER_SYMBOL = 28
    NOT_ASSIGNED = 29

class UnicodeNumericType(enum.IntEnum):
    NONE = 0
    DECIMAL = 1
    DIGIT = 2
    NUMERIC = 3

TextSegment = _ns_module.TextSegment
AlternateWordForm = _ns_module.AlternateWordForm
SelectableWordSegment = _ns_module.SelectableWordSegment
SelectableWordsSegmenter = _ns_module.SelectableWordsSegmenter
SemanticTextQuery = _ns_module.SemanticTextQuery
TextConversionGenerator = _ns_module.TextConversionGenerator
TextPhoneme = _ns_module.TextPhoneme
TextPredictionGenerator = _ns_module.TextPredictionGenerator
TextReverseConversionGenerator = _ns_module.TextReverseConversionGenerator
UnicodeCharacters = _ns_module.UnicodeCharacters
WordSegment = _ns_module.WordSegment
WordsSegmenter = _ns_module.WordsSegmenter
