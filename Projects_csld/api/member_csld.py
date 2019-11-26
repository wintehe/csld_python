import tornado.web
import tornado.ioloop
from common.uils import DeviceSign,GetConsul,GetShebei
from common.redis_token import Token
import json
from models.member_model import registers
from tornado import gen
from common.verify_csld import VerifyC


class MemberApi(tornado.web.RequestHandler):

    def get(self):
        datas = self.request.body
        data_dict = json.loads(datas)

        res = VerifyC().vericion(data_dict)
        if res is not None:
            if res["errcode"] == 4001:
                self.write({"message": "该设备未绑定", "success": False})
            elif res["errcode"] == 4002:
                self.write({"message": "该设备未注册", "success": False})
            elif res["errcode"] == 4003:
                self.write({"message": "sign错误", "success": False})
            elif res["errcode"] == 4004:
                self.write({"message": "token不能为空", "success": False})
            elif res["errcode"] == 4005:
                self.write({"message": "shopID不能为空", "success": False})
            elif res["errcode"] == 4006:
                self.write({"message": "不能为空", "success": False})
            elif res["errcode"] == 4007:
                self.write({"message": "该设备不存在", "success": False})
        else:
            m_args = registers().get_data()
            result = []
            for i in m_args:
                result.append({
                    "activation_code":i.activation_code
                })
            self.write(json.dumps(result))


