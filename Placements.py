# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:46:09 2024

@author: RAM_ANURAG
"""

from pydantic import BaseModel
class Placement(BaseModel):
    cgpa : float
    iq   : float

    
#what is pydantic 