# -*- coding: utf-8 -*-
import pprint
import re
from collections import defaultdict

import pandas as pd

trans_file = "/home/t/文档/kiosk翻译/kiosk_23122.xlsx"

df = pd.read_excel(trans_file, skiprows=1)

# for index, row in df.iterrows():
def get_all_trans():
    m = defaultdict(dict)
    for row in df.itertuples(index=False):
        # 这里可以对每一行的数据进行操作，例如打印该行数据
        # print(row)
        d = row._asdict()
        en_content = d.get("en")
        if en_content and en_content != d.get("th"):
            m[en_content] = d
    return m


def get_en_mapping():
    en_ts_path = "/home/t/workspace/kiosk-web-src/src/language/en-US/cer-shopflow/index.ts"
    with open(en_ts_path, "r") as f:
        content = f.read()

    # 使用正则表达式提取 key 和 value
    # matches = re.findall(r"(\w+):\s*'([^']*)'", content)
    matches = re.findall(r"(\w+):\s*'((?:[^'\\]|\\.)*)'", content)


    # 将提取的结果转换为 Python 字典
    # result_dict = {key: value.replace("\\'", "\'") for key, value in matches}
    # for k, v in matches:
    #     print(v)
    result_dict = {key: value for key, value in matches}
    return result_dict

zh_mapping = {
    "powerOn": {
        "selectRegisteredModel": "请选择注册机型",
        "contactAdministrator": "机型获取失败,请联系管理员",
        "selectModel": "请选择机型",
        "powerOff": "关机",
        "releaseStart": "开始解除",
        "locksCompleted": "锁紧全部完成",
        "saveConfig": "确认是否保存该配置?",
        "setOnce": "(仅可设置一次,请仔细核对配置)",
        "registering": "正在注册",
        "machineId": "机器ID为",
        "registeredSuccessfully": ["注册成功!", "s后", "重启机器"],
        "locksRemoved": "请确认以上所有位置锁紧均已拆除,如有遗漏会造成机器致命损伤!",
        "Initializing": "初始化中,请稍后...",
        "welcometoRoboshop": "欢迎进入机器人商店",
        "mechanismInit": "机器初始化中,请稍后",
        "networkInit": "网络初始化中, 请稍后",
        "booting": "正在启动,请稍后",
        "networkInitFailed": "网络初始化失败,请检查网络"
    },
    "home": {
        "userName": "用户名",
        "scanSuccess": "扫描成功",
        "supportPay": "支持微信、支付宝等",
        "passWord": "密码",
        "scanLogin": "扫码登录",
        "close": "关闭"
    },
    "shopping": {
        "slectCoupon": "请选择优惠券",
        "cashDeduction": "立减券",
        "discount": "折扣券",
        "off": "折",
        "orders": ["订单满", "使用"],
        "ordersPieces": ["订单满", "件使用"],
        "scanCode": "订单内包含限购商品,请扫码验证购买资质",
        "supportUse": "支持使用",
        "enterEmail": "请输入会员邮箱",
        "enterCorrectEmail": "请输入正确的邮箱",
        "selectGoods": "没有商品快去挑选商品吧",
        "goSettle": "去结算",
        "addCart": "加入购物车",
        "addSuccessfully": "添加成功,在购物车等你哦!",
        "consumptionTax": "消费税",
        "coupon": "优惠券优惠",
        "couponCode": "优惠码优惠",
        "reduction": "共减",
        "expand": "展开",
        "fold": "收起",
        "giftZone": "赠品区",
        "selectGift": "选择赠品",
        "cartEmpty": "哎呦,这里空空如也~",
        "goLook": "去逛一逛",
        "restricted": ["该商品限购", "件"],
        "maximum": "已达最大购买数量",
        "acquirePoints": "获取积分",
        "enterCouponCode": "输入优惠码",
        "additional": ["再买", "可再减"],
        "totalReduction": "共减",
        "detail": "明细",
        "goPay": "去支付",
        "warmTips": "温馨提示",
        "tips": "应国家法律法规要求,不得向8周岁以下的未成年人出售盲盒商品,8周岁以上未成年人购买盲盒商品,应通过线上线下等不同方式确认监护人同意。",
        "underage18": "未满18周岁",
        "overage18": "未满18周岁",
        "scanQR": "请扫描二维码,领取优惠券",
        "payCompleted": "支付完成,请稍后...",
        "suspendsSales": "机器暂停销售",
        "enterMobileNumber": "请输入手机号",
        "enterCode": "请输入编码",
        "enterLoveCode": "请输入爱心捐赠码",
        "enterCouponCode1": "请输入优惠码",
        "failedPass": "商品限购未通过",
        "onPayNotClose": "正在支付中不能关闭",
        "notbeableSubmit": ["会员", "未输入将无法积分,是否继续提交订单?"],
        "detailedParameters": "详细参数",
        "preSellTime": "预售时间",
        "parameters": "参数",
        "marketPrice": "市场价",
        "specifications": "规格",
        "seanGetCoupon": "扫码领优惠",
        "viewSwitching": "视图切换",
        "itisEmpty": "哎呦,这里空空如也~",
        "allMerchandise": "全部商品",
        "printTheInvoice": "发票打印",
        "unifiedInvoice": "打统编",
        "freeUnifiedInvoice": "免统编",
        "invoiceDonation": "发票捐赠",
        "loveDonation": "爱心捐赠",
        "selectSolt": "请选择货道购买商品",
        "collectionSuspended": "暂停领取",
        "tobeReplenish": "待补货",
        "ordered": "已预定",
        "enterEmails": "输入邮箱",
        "enterPhone": "输入手机号",
        "reduceDiscount": ["再买", "元可再减/打", "折"],
        "transactionFailed": "交易失败",
        "carrierID": "载具号码",
        "itemView": "商品视图",
        "operationTooFreq": "操作太频繁请稍后",
        "scanTips": "扫码提示",
        "invoiceBarcodeScanTips": "请出示手机条码并于扫描区扫码",
        "skipAndPrintInvoice": "跳过,直接打印发票",
        "scanCodeSuccess": "扫码成功",
        "invoiceDonateConfirm": "确认将发票爱心捐赠",
        "slotView": "货架视图",
        "gift": "赠",
        "amountDetail": "金额明细",
        "discountOnThresholdMet": "满减优惠",
        "decrease": "减",
        "input": "输入",
        "canMore": "可再",
        "underageSalesProhibition": "应国家法律法规要求,不得向8周岁以下的未成年人出售盲盒商品,8周岁以上未成年人购买盲盒商品,应通过线上线下等不同方式确认监护人同意。",
        "under8YearsOld": "未满8周岁",
        "over8YearsOld": "已满8周岁",
        "giftOutOfStock": "本机赠品已送完,买赠活动暂无赠品可选,是否仍然去支付?",
        "thinkAboutAgain": "我再想想",
        "payNow": "现在支付",
        "surpriseGiftOutOfStock": "本机惊喜礼品目前已赠罄,购买后无法获得赠品请您确认后再支付哦",
        "giftProbabilityConfirmation": ["此次购买有", "的概率获得赠品,请您确认后再支付哦"],
        "canNotReduceQtyFurther": "宝贝不能再减少了",
        "formatErrorTryAgain": "格式错误请重新输入",
        "pleaseSelectGift": "请选择赠品",
        "enterUnifiedCode": "请输入统一编号",
        "enterCorrectUnifiedCode": "请输入正确的统一编号",
        "enterCorrectDonateCode": "请输入正确的爱心捐赠码",
        "discountPrefix": "打",
        "salesSuspended": "暂停销售",
        "purchaseLimitNotice": "限购提示",
        "outOfStock": "已售罄",
        "purchase": "购买",
        "canGet": "可获得",
        "goGatherOrder": "去凑单",
        "alreadyGet": "已获得",
        "eligibleForPromotion": "已满足活动条件[去添加赠品]" ,
        "noAvailableCoupons": "没有可用的优惠券哦"
    },
    "planogram": {
        "default": "默认",
        "small_pendants": "小挂件/低位脱钩",
        "big_item": "大货物",
        "ipad4": "iPad4",
        "ipad": "Ipad",
        "bottle1": "瓶底",
        "fluency_3mm": "流利条A",
        "fluency_14mm": "流利条B",
        "bottom_noz": "下吸嘴",
        "top_noz": "上吸嘴",
        "default_r5": "默认(0, 21.7mm)",
        "light": "轻型货物",
        "egg_shaped_a": "蛋形取货",
        "instant_noodles_mode": "泡面模式",
        "pad_item": "平板模式",
        "heavy": "重型货物"
    },
    "payment": {
        "totalPrices": ["共", "件"],
        "tips": "请选择支付方式",
        "remainingTime": "支付剩余时间",
        "scanQRPay": "扫码付款",
        "giveUpPay": "是否放弃本次付款?",
        "goPay": "去支付",
        "continuePay": "继续支付",
        "AustralianDollar": "澳币",
        "HongKongDollar": "港币",
        "selectAnoterPay": "暂不支持使用,请选择其他支付方式",
        "least002": "消费金额至少需要消费0.02港币以上",
        "up6000": "仅支持60000港币以内消费使用",
        "least001": "消费金额至少需要消费0.1澳币以上",
        "up1000": "仅支持NT$1000以内消费使用",
        "notSupportd": "不支持该支付方式",
        "timeout": "支付返回结果超时,您可选择返回后重新支付。",
        "OrderCreationFailed": "创建订单失败,请重试",
        "paymentFaild": "支付失败",
        "callPhone": ['（若已支付可拨打','联系售后退款）'],
        "otherPay": '其他支付方式',
        "paySuccess": '如果您已经支付成功，单击“继续支付” 后无须再次付费',
        "selectScanMethod": '请选择扫码方式',
        "scanByWechat": '微信扫码',
        "scanByAlipay": '支付宝扫码',
        "pleaseUse": '请用',
        "scanToPay": '扫码支付',
    },
    "pickup": {
        "surpriseGift": "恭喜获得惊喜礼品",
        "shipped": "将跟随商品一起出货哦",
        "picking": "正在取货",
        "shipping": "正在出货",
        "pickingThe": ["正在取第", "件", "共", "商品"],
        "waitMonment": "请稍等片刻,不要离开哟",
        "shippingfinished": "完成出货",
        "pickupYourItems": "请从屏幕下方出货口取走您的商品",
        "confirmPickup": "确认已取走所有商品",
        "canceledOrder": "订单已取消",
        "willrRefunded": "已支付金额将自动退款,请放心",
        "pickupBottom": "请从屏幕下方取走您的商品",
        "continueToPick": "继续取货",
        "cold": "冷",
        "hot": "热"
    },
    "result": {
        "receipt": "小票",
        "orderNo": "单号",
        "time": "时间",
        "itemName": "商品名称",
        "unitPrice": "单价",
        "quantity": "数量",
        "discount": "优惠",
        "paymentMode": "支付方式",
        "merchantOrderNo": "商户单号",
        "getTheGift": "赠品领取方法",
        "redeemCode": "兑换码",
        "invoice": "如需索取商品发票请致电",
        "consumptionStub": "消费存根",
        "printSlip": "打印凭条",
        "problems": "遇到问题",
        "satisfied": "满意",
        "fair": "一般",
        "unsatisfactory": "不满意",
        "invoiceTemporarily": "机器暂时无法打印发票,请咨询",
        "gettinCode": "恭喜获得兑换码,赶快去使用吧",
        "useCode": ["恭喜获得兑换码", "赶快去使用吧"],
        "recordIt": "提示:页面退出即消失,赶快记录下来哦",
        "contactCustomer": "如果有问题可以联系客服小姐姐哦~",
        "customerCall": "客服电话",
        "rateExperience": "对本次购物体验打个评价吧",
        "successfulRating": "评价成功",
        "welcome": "欢迎光临",
        "phone": "电话",
        "congratulationOnObtain": "恭喜获得"
    },
    "goodsActivity": {
        "inputPickupCode": "输入提货码",
        "identifyQrCode": "识别二维码",
        "goodsActivity": "开心收下",
        "pickupBackHomeTips": "返回首页后,您的手机号将失去本次领赠活动资格,是否确定返回?",
        "goodsItemOut": "已赠罄"
    },
    "lottery": {
        "selectLuckyDrawNumber": "请选择抽奖次数",
        "give": "送",
        "draw": "抽",
        "kindlyTips": "温馨提示",
        "drawNumberGtZeroTips": "抽奖次数必须大于0",
        "drawNumberRequiredTips": "抽奖次数必填"
    },
    "questionnaire": {
        "discountShopping": "优惠购物",
        "clamGifts": "领取赠品",
        "inputPickupCode": "请输入提货码"
    }
}
