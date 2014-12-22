# -*- coding: utf-8 -*-
from SemanticNodes import *


templates = [

{"SemanticNode": Greeting,
 "body": [[{"kwords":["привет", "приветствовать", "здравствовать", "здар", "здаров", "здравие", "почтение"],
            "lexems":[],
            "required": True,
            "remember": False}, ], ],
 "chance": 8},

{"SemanticNode": Greeting,
 "body": [[{"kwords":["добрый", "отличный"],
            "lexems":[],
            "required": True,
            "remember": False},
           {"kwords":["вечер", "день", "утро", "денек", "утречко", "вечерок", "вечерочек"],
            "lexems":[],
            "required": True,
            "remember": False}, ], ],
 "chance": 8},

]