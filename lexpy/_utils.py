import re
from contextlib import closing

__all__ = ['validate_expression', 'gen_source']

PATTERN_FOR_WILDCARD_SEARCH = re.compile(r'(?:(\*\?)+|(\?\*)+|\*+)')
PATTERN_FOR_CONSECUTIVE_QUESTION_MARK = re.compile(r'\?+')


def validate_expression(wildcard_expression):
    """
    Description:
        Validates and shortens the wild card expression(if needed) without changing the intended meaning .

    Args:
        :arg (str) wild card expression

    Returns:
        :return (str) A shortened copy of the wild card expression.

    Raises:
        :raises (``InvalidWildCardExpressionError``) Any error while validating the expression.

    Example:
        >>> from lexpy._utils import validate_expression
        >>> sample_expr = 'a*?' # Match literal `a` followed by any character Zero or unlimited times.
        >>> print(validate_expression(sample_expr)) # Outputs 'a*'

    """
    # Replace with single *
    result = re.sub(PATTERN_FOR_WILDCARD_SEARCH, '*', wildcard_expression)

    # Replace with a single ?
    result = re.sub(PATTERN_FOR_CONSECUTIVE_QUESTION_MARK, '?', result)
    return result


def gen_source(source):
    """

    """
    if hasattr(source, 'read'):
        input_file = source
    else:
        input_file = open(source, 'r')

    with closing(input_file):
        for line in input_file:
            yield line.strip()



