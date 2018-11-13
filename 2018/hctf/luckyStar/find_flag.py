#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 hzshang <hzshang15@gmail.com>
#
# Distributed under terms of the MIT license.

t1="DEF0A07232EEBC954C11473ABD57E649".decode("hex")[::-1]
t2="05CCC8CA3C67C5A6A96E49835683F2AC".decode("hex")[::-1]
s=map(ord,t1+t2)
#xor_num = [22980,292,2906,10660,7730,32692,21856,32437,30932,2191,32198,5337,32682,12936,30123,14337,12529,7352,21068,4292,6644,18956,19066,31745,24613,22016,10316,1478,24684,26281,785,2928]
array = [7000,22058,9462,8438,313,31579,13607,25688,373,10432,31469,8295,16228,18912,29442,24839,20778,12002,13637,1451,25401,12797,21596,12910,13591,20783,24733,22368,21346,4146,4655,16925,13073,13996,24172,28069,4604,16038,31882,1127,16543,1855,7547,18591,14618,8097,23313,22242,10109,15925,8806,30455,18243,14355,7547,28393,14876,3261,24607,3162,15344,23052,23571,22554,22560,19562,24683,10233,1039,24386,10295,729,17121,437,15459,2823,13954,29583,11484,25291,16874,28281,25844,16189,8352,28528,7944,7515,6013,13429,15200,19801,8883,17030,32342,18488,17678,1998,31163,922,23673,28185,9590,14293,8131,29066,27502,19526,10659,3984,10923,24040,13562,8726,30136,5156,28249,31482,4171,14315,32451,21441,28711,16643,13236,25993,17730,19870,26721,15678,19747,14385,5186,8209,30095,16259,8910,5158,4708,29957,30854,24973,10949,25953,18740,8052,8567,12117,9077,8603,15499,31938,21877,23048,20542,4608,3834,763,4381,26485,25764,9508,20845,358,6259,19988,11721,31244,19337,2802,27917,29163,32049,31599,6003,23135,31521,4347,2300,20088,9980,20026,786,28167,13595,6833,363,28409,18573,32454,22064,22756,4188,23527,20831,7904,18962,29961,30574,2968,19836,23380,2865,13217,1454,4892,28413,25098,31559,1300,8462,13108,21495,4030,22310,20963,27454,19750,32119,2710,26742,24784,7363,10516,30227,25071,27586,21576,32298,13783,4036,23630,4144,28341,20631,11982,21509,638,17323,25993,11824,28197,12916,9009,31085,6417,16400,12926,31077,3278,4650,7038,27324,21763,286,9005,21584,7076,4957,26949,32192,21864,18452,6231,12076,4734,29960,23579,7740,18300,15300,4613,11364,8856,23031,26648,23142,16666,22808,24063,5400,22801,24907,23642,16231,11077,13192,22102,7580,20846,3834,10624,1502,15523,1445,12251,31224,30741,1100,14383,3677,1021,4498,22693,17001,23763,2143,20369,11754,705,20869,26255,10207,5463,24740,3025,19072,22400,30795,5559,30846,12213,31071,25760,18315,30832,16833,22273,29725,13540,24107,17332,17007,32235,4955,28306,28873,15168,628,11075,7938,31982,27809,8789,20291,2312,23035,27788,25613,29083,10157,30841,16254,18145,16725,28238,26576,14775,2478,1521,21794,16977,13933,847,19579,7981,9064,19699,27660,16453,24829,20695,19637,29321,434,11130,23755,24460,27417,17714,22553,13694,11767,22980,292,2906,10660,7730,32692,21856,32437,30932,2191,32198,5337,32682,12936,30123,14337,12529,7352,21068,4292,6644,18956,19066,31745,24613,22016,10316,1478,24684,26281,785,2928,22719,32761,21896,18708,20467,7231,17492,22046,12242,11757,10410,21816,17773,28318,13133,23406,7092,8023,15292,21135,25667,7693,4009,23254,25215,29800,22190,28617,3298,17351,24124,21602,22675,12932,25044,2669,25402,15993,9081,22833,28434,6339,26725,10066,25920,28357,11771,11254,21091,17520,11005,15143,4460,17346,28927,12665,6320,9613,16923,17132,7483,6010,28391,12563,103,17229,20644,11382,15278,23403,13240,25910,16061,20633,18015,3823,29641,5382,24477,23522,24102,4236,12919,13140,1814,10803,16738,10033,11487,2807,9724,27893,26656,32203,250,24012,15204,4317,9825]
array = array[383:]
pc = 0
# def get_rand():
# 	for i in array:
# 		yield i%4

for i in range(len(s)):
	s[i] ^= ((array[pc]%4)<<6)&0xff
	pc+=1
	s[i] ^= ((array[pc]%4)<<4)&0xff
	pc+=1
	s[i] ^= ((array[pc]%4)<<2)&0xff
	pc+=1
	s[i] ^= (array[pc]%4)&0xff
	pc+=1

print "".join(map(chr,s))
