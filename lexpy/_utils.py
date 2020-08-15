import re
from contextlib import closing

from lexpy.exceptions import InvalidWildCardExpressionError

__all__ = ['validate_expression', 'gen_source']

# A '?' followed by an '*' in the wildcard expr is illegal
__questionmark_after_asterisk_re = r'\?+(?=\*+)'
__questionmark_after_asterisk_pattern = re.compile(__questionmark_after_asterisk_re)


# Any special character apart from '*' or '?' is illegal.
__illegal_characters_re = r'[^\w?*]+'
__illegal_characters_pattern = re.compile(__illegal_characters_re)


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

    try:
        if re.search(__questionmark_after_asterisk_pattern, wildcard_expression) is not None:
            raise InvalidWildCardExpressionError(wildcard_expression,
                                                "A '?' followed by an '*' in the wildcard expr is illegal")

        if re.search(__illegal_characters_pattern, wildcard_expression) is not None:
            raise InvalidWildCardExpressionError(wildcard_expression, "Illegal Characters")

    except InvalidWildCardExpressionError as e:
        raise e
    result = re.sub('\*+', '*', wildcard_expression)  # Replace consecutive * with single *
    result = re.sub('\?+', '?', result)  # Replace consecutive ? with a single ?
    result = re.sub('(\*\?)+', '*', result)  # Replace consecutive '*?' with a single group '*'
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



