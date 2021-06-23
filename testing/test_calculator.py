# 1.改造 计算器 测试用例，使用 fixture 函数获取计算器的实例
#
# 2.计算之前打印开始计算，计算之后打印结束计算
#
# 3.添加用例日志，并将日志保存到日志文件目录下
#
# 4.生成测试报告，展示测试用例的标题，用例步骤，与测试日志，截图附到课程贴下
import allure
import pytest
import yaml
import logging


# 获取数据
def get_datas(method):
    with open(file='../datas/calculator.yaml', mode='r') as f:
        data = yaml.safe_load(f)
    return (data['data'][method], data['data'][f'ids_{method}'])


@allure.feature('计算器')
class TestCalculator:
    def setup(self):
        print('开始计算')

    def teardown(self):
        print('结束计算')

    @allure.story('这是常规加法story')
    @allure.title('这是常规加法title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('add')[0], ids=get_datas('add')[1])
    def test_add(self, a, b, expect, get_calculator):
        logging.debug(f'{a} + {b} == {expect}')
        assert expect == get_calculator.add(a, b)

    @allure.story('这是常规减法story')
    @allure.title('这是常规减法title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('subtraction')[0], ids=get_datas('subtraction')[1])
    def test_subtraction(self, a, b, expect, get_calculator):
        logging.debug(f'{a} - {b} == {expect}')
        assert expect == get_calculator.subtraction(a, b)

    @allure.story('这是常规乘法story')
    @allure.title('这是常规乘法title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('multiplication')[0], ids=get_datas('multiplication')[1])
    def test_multiplication(self, a, b, expect, get_calculator):
        logging.debug(f'{a} * {b} == {expect}')
        assert expect == get_calculator.multiplication(a, b)

    @allure.story('这是常规除法story')
    @allure.title('这是常规title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('division')[0], ids=get_datas('division')[1])
    def test_division(self, a, b, expect, get_calculator):
        logging.debug(f'{a} / {b} == {expect}')
        assert expect == get_calculator.division(a, b)

    @allure.story('除数为0的情况story')
    @allure.title('除数为0的情况title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('divisor_zero')[0], ids=get_datas('divisor_zero')[1])
    def test_division_divisor_is_zero(self, a, b, expect, get_calculator):
        logging.debug(f'{a} / {b} =={expect}')
        with pytest.raises(ZeroDivisionError):
            get_calculator.division(a, b)

    @allure.story('两小数相加的情况story')
    @allure.title('两小数相加的情况title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('decimals_add')[0], ids=get_datas('decimals_add')[1])
    def test_add_decimals_not_equal(self,a,b,expect,get_calculator):
        logging.debug(f'{a} + {b} = {expect}')
        with pytest.raises(AssertionError):
            assert expect == get_calculator.add(a,b)


    @allure.story('两小数相减的情况story')
    @allure.title('两小数相减的情况title')
    @pytest.mark.parametrize('a,b,expect', argvalues=get_datas('decimals_subtraction')[0], ids=get_datas('decimals_subtraction')[1])
    def test_subtraction_decimals_not_equal(self,a,b,expect,get_calculator):
        logging.debug(f'{a} - {b} = {expect}')
        with pytest.raises(AssertionError):
            assert expect == get_calculator.subtraction(a,b)

    @allure.story('图片和图片的stroy')
    @allure.title('视频和图片的title')
    def test_allure_video_and_photo(self):
        with allure.step('视频'):
            allure.attach.file(source='../datas/demo_video.mp4',
                               name='这是视频',
                               attachment_type=allure.attachment_type.MP4)
        with allure.step('图片'):
            allure.attach.file(source='../datas/demo_photo.png',
                               name='这是图片',
                               attachment_type=allure.attachment_type.PNG)