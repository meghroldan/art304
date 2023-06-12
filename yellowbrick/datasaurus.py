# yellowbrick.datasaurus
# Plots a Datasaurus Quartet as an illustration of the importance of visualization.
#
# Author:   Larry Gray
# Created:  Wed Jun 20 15:17:35 2018 -0400
#
# Copyright (C) 2018 The sckit-yb developers
# For license information, see LICENSE.txt
#
# ID: datasaurus.py [e49d780] lwgray@gmail.com $

"""
Plots a Datasaurus Quartet as an illustration of the importance of visualization.
"""

##########################################################################
## Imports
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

from yellowbrick.bestfit import draw_best_fit
from yellowbrick.style import get_color_cycle


##########################################################################
## DATASAURUS Data Arrays
##########################################################################

DATASAURUS = [
    np.array(
        [
            [
                55.3846,
                51.5385,
                46.1538,
                42.8205,
                40.7692,
                38.7179,
                35.641,
                33.0769,
                28.9744,
                26.1538,
                23.0769,
                22.3077,
                22.3077,
                23.3333,
                25.8974,
                29.4872,
                32.8205,
                35.3846,
                40.2564,
                44.1026,
                46.6667,
                50.0,
                53.0769,
                56.6667,
                59.2308,
                61.2821,
                61.5385,
                61.7949,
                57.4359,
                54.8718,
                52.5641,
                48.2051,
                49.4872,
                51.0256,
                45.3846,
                42.8205,
                38.7179,
                35.1282,
                32.5641,
                30.0,
                33.5897,
                36.6667,
                38.2051,
                29.7436,
                29.7436,
                30.0,
                32.0513,
                35.8974,
                41.0256,
                44.1026,
                47.1795,
                49.4872,
                51.5385,
                53.5897,
                55.1282,
                56.6667,
                59.2308,
                62.3077,
                64.8718,
                67.9487,
                70.5128,
                71.5385,
                71.5385,
                69.4872,
                46.9231,
                48.2051,
                50.0,
                53.0769,
                55.3846,
                56.6667,
                56.1538,
                53.8462,
                51.2821,
                50.0,
                47.9487,
                29.7436,
                29.7436,
                31.2821,
                57.9487,
                61.7949,
                64.8718,
                68.4615,
                70.7692,
                72.0513,
                73.8462,
                75.1282,
                76.6667,
                77.6923,
                79.7436,
                81.7949,
                83.3333,
                85.1282,
                86.4103,
                87.9487,
                89.4872,
                93.3333,
                95.3846,
                98.2051,
                56.6667,
                59.2308,
                60.7692,
                63.0769,
                64.1026,
                64.359,
                74.359,
                71.2821,
                67.9487,
                65.8974,
                63.0769,
                61.2821,
                58.7179,
                55.1282,
                52.3077,
                49.7436,
                47.4359,
                44.8718,
                48.7179,
                51.2821,
                54.1026,
                56.1538,
                52.0513,
                48.7179,
                47.1795,
                46.1538,
                50.5128,
                53.8462,
                57.4359,
                60.0,
                64.1026,
                66.9231,
                71.2821,
                74.359,
                78.2051,
                67.9487,
                68.4615,
                68.2051,
                37.6923,
                39.4872,
                91.2821,
                50.0,
                47.9487,
                44.1026,
            ],
            [
                97.1795,
                96.0256,
                94.4872,
                91.4103,
                88.3333,
                84.8718,
                79.8718,
                77.5641,
                74.4872,
                71.4103,
                66.4103,
                61.7949,
                57.1795,
                52.9487,
                51.0256,
                51.0256,
                51.0256,
                51.4103,
                51.4103,
                52.9487,
                54.1026,
                55.2564,
                55.641,
                56.0256,
                57.9487,
                62.1795,
                66.4103,
                69.1026,
                55.2564,
                49.8718,
                46.0256,
                38.3333,
                42.1795,
                44.1026,
                36.4103,
                32.5641,
                31.4103,
                30.2564,
                32.1795,
                36.7949,
                41.4103,
                45.641,
                49.1026,
                36.0256,
                32.1795,
                29.1026,
                26.7949,
                25.2564,
                25.2564,
                25.641,
                28.718,
                31.4103,
                34.8718,
                37.5641,
                40.641,
                42.1795,
                44.4872,
                46.0256,
                46.7949,
                47.9487,
                53.718,
                60.641,
                64.4872,
                69.4872,
                79.8718,
                84.1026,
                85.2564,
                85.2564,
                86.0256,
                86.0256,
                82.9487,
                80.641,
                78.718,
                78.718,
                77.5641,
                59.8718,
                62.1795,
                62.5641,
                99.4872,
                99.1026,
                97.5641,
                94.1026,
                91.0256,
                86.4103,
                83.3333,
                79.1026,
                75.2564,
                71.4103,
                66.7949,
                60.2564,
                55.2564,
                51.4103,
                47.5641,
                46.0256,
                42.5641,
                39.8718,
                36.7949,
                33.718,
                40.641,
                38.3333,
                33.718,
                29.1026,
                25.2564,
                24.1026,
                22.9487,
                22.9487,
                22.1795,
                20.2564,
                19.1026,
                19.1026,
                18.3333,
                18.3333,
                18.3333,
                17.5641,
                16.0256,
                13.718,
                14.8718,
                14.8718,
                14.8718,
                14.1026,
                12.5641,
                11.0256,
                9.8718,
                6.0256,
                9.4872,
                10.2564,
                10.2564,
                10.641,
                10.641,
                10.641,
                10.641,
                10.641,
                10.641,
                8.718,
                5.2564,
                2.9487,
                25.7692,
                25.3846,
                41.5385,
                95.7692,
                95.0,
                92.6923,
            ],
        ]
    ),
    np.array(
        [
            [
                51.20389114,
                58.9744699,
                51.87207267,
                48.17993079,
                41.6832004,
                37.8904155,
                39.54897369,
                39.64957388,
                34.75059705,
                27.56083529,
                24.63553998,
                20.95946481,
                20.68914905,
                19.28820474,
                20.02450057,
                35.469523,
                36.89432765,
                39.05554978,
                46.95708015,
                37.31045274,
                40.009672,
                48.01438668,
                53.70377593,
                63.06749989,
                62.04803251,
                59.83996671,
                55.16094182,
                61.27978658,
                60.83491753,
                61.52059065,
                36.91654386,
                38.50219967,
                48.66437073,
                50.2852524,
                42.27633267,
                54.03177562,
                37.32935526,
                41.38952255,
                40.07466666,
                35.34968062,
                34.76370042,
                37.02662945,
                36.45556953,
                35.53766421,
                20.40894789,
                23.49571047,
                29.55754336,
                33.00823391,
                53.98039918,
                52.2343086,
                59.50307661,
                41.16378107,
                48.99304012,
                59.26928032,
                45.469177,
                62.69126654,
                73.42867087,
                70.84642611,
                71.53901985,
                67.62086589,
                72.47095256,
                64.81223756,
                60.85367987,
                67.78949616,
                41.60955727,
                53.00302532,
                54.71417106,
                44.29166872,
                49.19172196,
                53.10138178,
                51.59984815,
                54.37972195,
                46.4807681,
                53.17465627,
                45.27200294,
                36.03340215,
                28.27119417,
                25.05480608,
                64.758887,
                63.14452748,
                50.42467869,
                70.64499626,
                63.14904908,
                62.82402452,
                70.23686951,
                70.04273524,
                72.57062345,
                75.13071604,
                83.29390573,
                79.66426228,
                88.43210253,
                89.11555901,
                89.09219763,
                91.72600577,
                91.73553876,
                91.50788817,
                88.2390019,
                88.5305192,
                55.36516034,
                62.56025887,
                58.00666912,
                55.06711799,
                61.61477596,
                68.54314354,
                77.70610965,
                68.453046,
                68.25720644,
                70.25547467,
                65.04432528,
                60.09224661,
                52.99202897,
                50.14462898,
                46.50861419,
                43.80703196,
                57.81785469,
                50.94049266,
                63.49732308,
                50.01648295,
                58.63676508,
                54.73028909,
                65.8755478,
                57.06098271,
                46.81990795,
                38.35939487,
                47.31541578,
                55.05191654,
                50.51596026,
                49.67741465,
                67.28065952,
                66.17301826,
                61.08854414,
                66.05308577,
                72.66998927,
                61.5034725,
                68.99502863,
                78.24991617,
                36.48198057,
                50.96774838,
                91.19105361,
                55.86376849,
                49.2805948,
                43.36850154,
            ],
            [
                83.33977661,
                85.49981761,
                85.82973763,
                85.04511674,
                84.0179406,
                82.567493,
                80.81260177,
                82.66453387,
                80.01109099,
                72.84782559,
                71.61071483,
                66.04149838,
                62.72130521,
                62.06305936,
                61.34262387,
                43.11588495,
                47.70655597,
                55.54697371,
                65.24040739,
                45.2587509,
                60.98658251,
                65.71281959,
                66.38948204,
                64.03500046,
                63.84586325,
                64.47676444,
                65.23730817,
                65.7664025,
                64.60376971,
                64.79185504,
                41.09524744,
                41.56715562,
                30.68066685,
                30.33792211,
                34.52763612,
                29.67234831,
                39.60204231,
                37.29605623,
                34.6236852,
                47.14107313,
                47.62479992,
                44.46229305,
                40.79184303,
                48.72938687,
                32.20303042,
                25.32246815,
                21.36477746,
                15.98507146,
                29.35098671,
                29.71167299,
                30.66967394,
                34.31575825,
                32.03035884,
                29.64070177,
                33.83119273,
                30.29037383,
                48.57785513,
                52.28225333,
                45.52180616,
                38.00655847,
                51.12213482,
                62.81091559,
                65.49914703,
                61.36370155,
                83.84868656,
                84.6747986,
                84.04312807,
                82.90944121,
                85.87622912,
                84.54765869,
                84.81982149,
                84.24035555,
                83.51821167,
                84.26056799,
                85.23707942,
                53.37168776,
                72.84023126,
                71.54859792,
                82.31522364,
                85.23669633,
                85.17474759,
                82.43091876,
                83.94685535,
                84.96618595,
                82.17115106,
                80.38502135,
                80.97121843,
                79.98409314,
                70.77843179,
                73.93230972,
                64.624247,
                64.00150664,
                57.76819305,
                52.62335326,
                48.97021089,
                53.31265209,
                31.47743488,
                30.47603101,
                30.44585028,
                30.44713567,
                30.2537213,
                29.0115352,
                29.99439119,
                35.65783217,
                20.30426019,
                13.03552859,
                12.38463915,
                13.25038497,
                11.00084148,
                11.87211171,
                9.90666848,
                12.21154309,
                11.20713449,
                11.31894489,
                10.94514243,
                9.69154713,
                11.91406917,
                11.93385209,
                11.97472107,
                11.41288267,
                11.73243636,
                9.92056085,
                10.49465268,
                13.43132262,
                12.85345178,
                11.94998862,
                9.76559162,
                10.38313251,
                14.12865153,
                12.03791702,
                10.08453441,
                13.38022601,
                15.23422594,
                10.82841448,
                13.99431053,
                17.88324091,
                15.16276009,
                29.67977429,
                46.67434284,
                85.33648676,
                84.04882283,
                84.3321772,
            ],
        ]
    ),
    np.array(
        [
            [
                58.21360826,
                58.19605369,
                58.71823072,
                57.27837287,
                58.08202049,
                57.48944777,
                28.08874132,
                28.08546821,
                28.08727305,
                27.57802522,
                27.77991911,
                28.58899981,
                28.7391415,
                27.02460324,
                28.8013367,
                27.18646384,
                29.2851466,
                39.4029453,
                28.81132844,
                34.30395791,
                29.60276098,
                49.11615686,
                39.61754583,
                43.23308466,
                64.89278794,
                62.49014932,
                68.98808443,
                62.10561863,
                32.46184674,
                41.32720065,
                44.00714993,
                44.07406069,
                44.00131524,
                45.00630045,
                44.44384061,
                42.1787134,
                44.04456562,
                41.64045402,
                41.93833001,
                44.05392751,
                39.20671933,
                28.70444923,
                31.7086629,
                42.81171147,
                43.30061489,
                40.39863291,
                40.43569158,
                40.93654667,
                39.66157367,
                40.89925917,
                41.96861683,
                40.38340582,
                56.53812645,
                52.97069128,
                54.62095259,
                65.09904439,
                63.05599091,
                70.96013623,
                69.89581924,
                70.59589286,
                69.64702143,
                77.39298249,
                64.40078719,
                63.86895983,
                56.59442132,
                56.53133729,
                59.65215837,
                56.6365087,
                58.672288,
                58.22161273,
                57.91466448,
                55.31550906,
                54.57572859,
                54.41309365,
                55.0745059,
                29.43296052,
                29.42268607,
                29.00561416,
                58.46183859,
                57.99780474,
                57.54947408,
                59.52992846,
                58.24939106,
                58.02451401,
                58.38212449,
                62.56675904,
                72.17582431,
                79.47276157,
                80.35770088,
                78.75723614,
                82.54023959,
                86.43589719,
                79.48868442,
                81.53042032,
                79.18678857,
                77.89905795,
                75.13071421,
                76.05801375,
                57.61467439,
                56.17139753,
                66.2878906,
                67.88171962,
                64.0280813,
                77.49665175,
                77.63465176,
                77.86372643,
                77.33815817,
                76.18041653,
                77.25265109,
                77.41337528,
                76.7318494,
                49.47110541,
                42.47653994,
                43.59511586,
                50.33996967,
                40.74898026,
                38.38652558,
                38.40401521,
                38.76427889,
                41.47014233,
                47.15540481,
                39.58256675,
                41.74024382,
                39.31187189,
                41.67984769,
                39.08746445,
                41.48150286,
                77.60608655,
                75.98266152,
                76.94575724,
                77.54372007,
                77.58473984,
                76.82230426,
                77.34857166,
                77.57315269,
                77.97261068,
                41.52891976,
                43.7225508,
                79.32607818,
                56.66397408,
                57.82178923,
                58.2431719,
            ],
            [
                91.88189151,
                92.21498865,
                90.31053209,
                89.90760672,
                92.00814501,
                88.08528556,
                63.51079443,
                63.59019695,
                63.12328281,
                62.82103866,
                63.51814752,
                63.02408057,
                62.72086389,
                62.90185886,
                63.38904039,
                63.55872965,
                63.38360583,
                51.1508572,
                61.35785406,
                56.54212591,
                60.15734672,
                63.66000062,
                62.92518796,
                63.16521872,
                65.81417676,
                74.58428961,
                63.2321473,
                75.99087076,
                62.88190292,
                49.07025127,
                46.44967378,
                34.55320389,
                33.90420735,
                38.29901955,
                36.0190833,
                26.49211948,
                35.66223828,
                27.09309542,
                24.99152298,
                33.55639249,
                51.5337157,
                61.7775254,
                58.83775437,
                30.02044842,
                31.5264262,
                16.34700838,
                20.23267068,
                16.91300484,
                15.60935558,
                20.79852895,
                26.4970726,
                21.39122552,
                32.44424547,
                29.04019669,
                30.34452445,
                27.24155756,
                29.70909567,
                41.25950129,
                43.45375927,
                41.96474387,
                44.04444502,
                63.37145906,
                67.44871845,
                70.21373883,
                86.92700622,
                87.49981107,
                87.80946159,
                85.63749556,
                90.07716031,
                90.41101877,
                89.95380277,
                80.25186069,
                77.53628847,
                78.22908659,
                79.81754642,
                60.80177654,
                63.06846482,
                63.39075133,
                90.26532639,
                92.15990861,
                90.74890656,
                88.32727415,
                92.12968148,
                91.69442117,
                90.55347607,
                77.74393476,
                63.12892942,
                63.40868612,
                63.29543754,
                53.33262001,
                56.54105229,
                59.79276181,
                53.65167426,
                56.02536457,
                53.23479185,
                51.82245833,
                23.37244197,
                16.38374969,
                33.82244765,
                32.11798877,
                26.11710975,
                24.23601841,
                27.67268551,
                14.94852356,
                14.46185393,
                14.61067765,
                15.89005466,
                15.91257375,
                15.15151702,
                15.22192798,
                16.21684614,
                25.06301931,
                18.33847356,
                19.99420098,
                26.47139661,
                16.18214166,
                14.58021515,
                14.45194845,
                14.36559047,
                17.27803344,
                22.37793253,
                17.64845284,
                17.82932431,
                15.64071697,
                17.74591901,
                15.12230394,
                18.04743744,
                15.16287254,
                16.30692238,
                15.85847833,
                15.25394915,
                15.83003939,
                15.59516532,
                15.77452924,
                14.78064583,
                14.95569875,
                24.91642519,
                19.0773278,
                52.90039129,
                87.94012501,
                90.69316655,
                92.10432787,
            ],
        ]
    ),
    np.array(
        [
            [
                51.14791671,
                50.51712581,
                50.2074802,
                50.06948192,
                50.56284634,
                50.2885278,
                25.58347508,
                25.48358339,
                25.4435257,
                25.56511342,
                25.92884427,
                27.55147826,
                27.53046637,
                27.09557036,
                27.43924961,
                27.87826426,
                27.33886892,
                27.67840297,
                52.63565768,
                52.02521411,
                52.88116479,
                52.95260731,
                52.52055249,
                52.34282206,
                51.92759021,
                52.71377449,
                50.44380279,
                50.21669503,
                52.18418011,
                52.79209735,
                52.58971986,
                52.02884867,
                52.72924658,
                52.88431329,
                52.50930089,
                50.86268433,
                50.89149225,
                25.8551276,
                26.02564455,
                27.89317272,
                27.63996794,
                27.8926589,
                52.79773294,
                27.58063881,
                26.49139853,
                25.98531782,
                26.20141928,
                25.85756947,
                50.70468436,
                50.81197535,
                50.56484556,
                50.93930391,
                50.45885484,
                52.90136407,
                52.68495344,
                52.50008894,
                51.83563726,
                76.9954121,
                77.31060048,
                77.92604434,
                77.25438834,
                76.2431578,
                77.08448437,
                75.2280532,
                50.65835477,
                50.20336581,
                50.9295477,
                50.17867185,
                50.42269806,
                50.46422483,
                50.44927033,
                49.92838028,
                50.48801364,
                49.96490538,
                50.75210826,
                27.42242921,
                27.6740834,
                27.53739532,
                52.26334738,
                51.73728166,
                75.87096369,
                75.24432621,
                75.19829529,
                75.70104153,
                75.47933966,
                75.19456687,
                74.82025396,
                75.16434049,
                75.26335555,
                77.75641893,
                77.95443505,
                77.08333777,
                76.06355025,
                77.68201632,
                76.87808198,
                76.94850272,
                77.86405471,
                75.77145009,
                52.33156913,
                52.59281837,
                50.47704772,
                75.29647509,
                75.57395413,
                75.40052716,
                75.87099084,
                75.60588476,
                75.89557705,
                75.7465632,
                75.14234148,
                50.66177956,
                50.69985064,
                50.91894087,
                50.72525854,
                51.26387123,
                51.25091965,
                50.78515721,
                50.50139658,
                50.73367454,
                50.71137854,
                50.8127449,
                51.01423295,
                50.35352141,
                50.43552957,
                50.63098196,
                51.0668072,
                50.79235473,
                50.55127806,
                50.55975806,
                75.32597855,
                75.04472578,
                75.28708772,
                75.23996998,
                75.1524592,
                75.96184009,
                75.44806251,
                75.75938382,
                50.3782623,
                50.53363501,
                77.50090732,
                50.69112419,
                49.99039495,
                50.12718203,
            ],
            [
                90.86741233,
                89.10239459,
                85.4600474,
                83.05766953,
                82.93782178,
                82.97525357,
                82.91489113,
                82.92908498,
                82.8742005,
                82.92409777,
                82.82118411,
                51.48738653,
                51.41484656,
                52.07679944,
                51.71207905,
                50.70890793,
                51.65304675,
                51.18198917,
                51.41855226,
                52.12301105,
                50.62155476,
                50.07473901,
                51.5024421,
                51.86195209,
                52.25779061,
                51.19794432,
                82.94182882,
                83.75234297,
                51.97525067,
                51.07339565,
                51.3380902,
                52.1768375,
                51.20176505,
                50.44143545,
                51.41620515,
                17.14563109,
                17.14132373,
                17.08190869,
                16.92501353,
                50.66196341,
                51.39909748,
                50.79528152,
                50.68603709,
                51.52476126,
                17.40539097,
                17.20372213,
                17.09382391,
                17.11384266,
                17.02374454,
                17.11492526,
                17.07777732,
                16.98102188,
                17.03857897,
                50.69056272,
                51.29446922,
                51.59435617,
                52.33576553,
                52.04552865,
                51.74673004,
                50.31866042,
                51.46182482,
                52.12368985,
                51.9671367,
                82.98566202,
                83.11447934,
                82.98265686,
                82.84604113,
                83.18462233,
                82.90990147,
                82.93532841,
                83.96992038,
                82.99366549,
                83.09951912,
                83.7083177,
                82.9019501,
                51.43887623,
                51.30411215,
                51.59365408,
                94.24932783,
                92.97911753,
                88.38644174,
                83.90349738,
                83.46230334,
                82.91945886,
                82.88405139,
                82.93211578,
                82.96238879,
                83.03499717,
                82.9452793,
                51.15177033,
                50.47557897,
                52.15779927,
                52.10465206,
                51.16563781,
                51.8675623,
                51.90751654,
                49.66254553,
                17.11125121,
                51.87886035,
                51.39159152,
                17.04828941,
                17.01565319,
                17.06219214,
                17.04110689,
                17.13489391,
                17.06772306,
                17.16994971,
                17.10571651,
                16.75492389,
                17.07814052,
                17.08518438,
                17.14760476,
                16.90746981,
                17.16234971,
                17.24045586,
                17.18019648,
                17.10577072,
                16.99296341,
                17.08831585,
                16.57271805,
                17.22109553,
                17.06474308,
                17.0651685,
                17.07652235,
                17.20885971,
                17.20421434,
                17.08465518,
                17.09388377,
                15.77189199,
                17.00426226,
                16.17493491,
                17.03184749,
                17.0049424,
                16.69484223,
                17.04514941,
                16.94292965,
                16.94627981,
                17.01958137,
                50.16698595,
                87.51396042,
                83.99735692,
                82.99075,
            ],
        ]
    ),
]


def datasaurus():
    """
    Creates 2x2 grid plot of 4 from the Datasaurus Dozen datasets for illustration.

    Citation:
    Justin Matejka, George Fitzmaurice (2017)
    Same Stats, Different Graphs: Generating Datasets with Varied Appearance and
    Identical Statistics through Simulated Annealing
    CHI 2017 Conference proceedings:
    ACM SIGCHI Conference on Human Factors in Computing Systems
    """
    _, ((axa, axb), (axc, axd)) = plt.subplots(2, 2, sharex="col", sharey="row")
    colors = get_color_cycle()
    for arr, ax, color in zip(DATASAURUS, (axa, axb, axc, axd), colors):
        x = arr[0]
        y = arr[1]

        # Draw the points in the scatter plot
        ax.scatter(x, y, color=color)

        # Set the X and Y limits
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 110)

        # Draw the linear best fit line on the plot
        draw_best_fit(x, y, ax, c=color)

    return (axa, axb, axc, axd)


if __name__ == "__main__":
    datasaurus()
    plt.show()
