"""Auto-generated file, do not edit by hand. IE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IE = PhoneMetadata(id='IE', country_code=353, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[124-9]\\d{6,9}', possible_length=(7, 8, 9, 10), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{7,8}|2(?:1\\d{6,7}|3\\d{7}|[24-9]\\d{5})|4(?:0[24]\\d{5}|[1-469]\\d{7}|5\\d{6}|7\\d{5}|8[0-46-9]\\d{7})|5(?:0[45]\\d{5}|1\\d{6}|[23679]\\d{7}|8\\d{5})|6(?:1\\d{6}|[237-9]\\d{5}|[4-6]\\d{7})|7[14]\\d{7}|9(?:1\\d{6}|[04]\\d{7}|[35-9]\\d{5})', example_number='2212345', possible_length=(7, 8, 9, 10), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='8(?:22\\d{6}|[35-9]\\d{7})', example_number='850123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', example_number='1800123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='15(?:1[2-8]|[2-8]0|9[089])\\d{6}', example_number='1520123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='18[59]0\\d{6}', example_number='1850123456', possible_length=(10,)),
    personal_number=PhoneNumberDesc(national_number_pattern='700\\d{6}', example_number='700123456', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='76\\d{7}', example_number='761234567', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='818\\d{6}', example_number='818123456', possible_length=(9,)),
    voicemail=PhoneNumberDesc(national_number_pattern='8[35-9]5\\d{7}', example_number='8551234567', possible_length=(10,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='18[59]0\\d{6}', example_number='1850123456', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(1)(\\d{3,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['2[24-9]|47|58|6[237-9]|9[35-9]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['40[24]|50[45]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(48)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['48'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(818)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['818'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[24-69]|7[14]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['76|8[35-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(8\\d)(\\d)(\\d{3})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['8[35-9]5'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(700)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['700'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:5|8[059])', '1(?:5|8[059]0)'], national_prefix_formatting_rule='\\1')],
    mobile_number_portable_region=True)
