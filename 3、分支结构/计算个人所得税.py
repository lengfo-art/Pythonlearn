# -*- coding: utf-8 -*-
"""
File Name

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""

"""
2025年最新个人所得税计算器（按月预扣预缴）
说明：
代码结构：
    输入月收入。
    计算应纳税所得额 = 月收入 - 5000
    如果应纳税所得额 ≤0，税额为0。
    否则，根据税率表计算税额。
    税率表可以用列表或字典表示。例如，使用列表，每个元素包含上限、税率、速算扣除数。
    税率表结构：
    rate_table = [
    (3000, 0.03, 0),
    (12000, 0.10, 210),
    (25000, 0.20, 1410),
    (35000, 0.25, 2660),
    (55000, 0.30, 4410),
    (80000, 0.35, 7160),
    (float('inf'), 0.45, 15160)
    ]
    
    
    个人所得税税率表一
    级数	累计预扣预缴应纳税所得额	预扣率（%）	速算扣除数
    1	不超过36,000元的部分	3	0
    2	超过36,000元至144,000元的部分	10	2520
    3	超过144,000元至300,000元的部分	20	16920
    4	超过300,000元至420,000元的部分	25	31920
    5	超过420,000元至660,000元的部分	30	52920
    6	超过660,000元至960,000元的部分	35	85920
    7	超过960,000元的部分	45	181920

    然后遍历税率表，找到第一个应纳税所得额 <= 上限的项，计算税额。
version: 0.2
author: 林风
Date: 2025-04-10
"""

def calculate_taxes(monthly_income):
    """
    2025年个人所得税计算器（按月预扣预缴）
    税率表：7级超额累进税率（基于月应纳税所得额）
    """
    deduction = 5000  # 起征点
    taxable_income = monthly_income - deduction
    
    if taxable_income <= 0:
        return 0.0
    
    # 月度税率表（包含速算扣除数）
    tax_table = [
        (3000, 0.03, 0),
        (12000, 0.10, 210),
        (25000, 0.20, 1410),
        (35000, 0.25, 2660),
        (55000, 0.30, 4410),
        (80000, 0.35, 7160),
        (float('inf'), 0.45, 15160)
    ]
    
    for threshold, rate, quick_deduction in tax_table: # 遍历税率表 
        if taxable_income <= threshold:              # 找到第一个应纳税所得额 <= 上限的项
            tax = taxable_income * rate - quick_deduction       # 计算税额
            return round(tax, 2)            # 保留两位小数
    
    return 0.0

# 用户交互界面
if __name__ == "__main__":
    try:
        monthly_income = float(input("请输入您的月收入（人民币）："))
        tax = calculate_taxes(monthly_income)
        taxable_income = monthly_income - 5000
        
        print("\n计算结果：")
        print(f"应纳税所得额：{taxable_income}元")
        print(f"应缴个人所得税：{tax}元")
        
    except ValueError:
        print("输入错误，请确保输入的是有效数字！")