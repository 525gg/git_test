import random
import shutil
def fuzhi(s):
    test = random.sample(range(1,60), 30)
    for i in test:
        i1 = str(i)
        if len(i1) == 1:
            i2 = 'MVI_'+s+'__img000'+i1+'0.jpg'
            t1='MVI_'+s+'__img000'+i1+'0.txt'
            print(i1)
        else:
            i2 = 'MVI_'+s+'__img00'+i1+'0.jpg'
            t1 = 'MVI_'+s+'__img00' + i1 + '0.txt'
            print(i1)
        ii1 = 'D:/download_edge/UA-DETRAC-G2/images/train/'+i2
        ii2 = 'D:/download_edge/UA-DETRAC-G2/images/val/'+i2
        ii3 = 'D:/download_edge/UA-DETRAC-G2/labels/train/'+t1
        ii4 = 'D:/download_edge/UA-DETRAC-G2/labels/val/'+t1
        print(ii1)
        print(ii3)
        try:
            shutil.move(ii1,ii2)
            shutil.move(ii3,ii4)
        except:
            print("失败")

fuzhi('20012')
fuzhi('20032')
fuzhi('20033')
fuzhi('20034')
fuzhi('20035')
fuzhi('20051')
fuzhi('20052')
fuzhi('20061')
fuzhi('20062')
fuzhi('20063')
fuzhi('20064')
fuzhi('20065')
fuzhi('39031')
fuzhi('39051')
fuzhi('39211')
fuzhi('39271')
fuzhi('39311')
fuzhi('39361')
fuzhi('39371')
fuzhi('39401')
fuzhi('39501')
fuzhi('39511')
fuzhi('39761')
fuzhi('39771')
fuzhi('39781')
fuzhi('39801')
fuzhi('39811')
fuzhi('39821')
fuzhi('39851')
fuzhi('39861')
fuzhi('39931')
fuzhi('40131')
fuzhi('40141')
fuzhi('40152')
fuzhi('40161')
fuzhi('40162')
fuzhi('40171')
fuzhi('40172')
fuzhi('40181')
fuzhi('40191')
fuzhi('40192')
fuzhi('40201')
fuzhi('40204')
fuzhi('40211')
fuzhi('40212')
fuzhi('40213')
fuzhi('40241')
fuzhi('40243')
fuzhi('40244')
fuzhi('40701')
fuzhi('40711')
fuzhi('40712')
fuzhi('40714')
fuzhi('40732')
fuzhi('40742')
fuzhi('40743')
fuzhi('40751')
fuzhi('40752')
fuzhi('40761')
fuzhi('40762')
fuzhi('40763')
fuzhi('40771')
fuzhi('40772')
fuzhi('40773')
fuzhi('40774')
fuzhi('40775')
fuzhi('40792')
fuzhi('40793')
fuzhi('40852')
fuzhi('40853')
fuzhi('40854')
fuzhi('40855')
fuzhi('40863')
fuzhi('40864')
fuzhi('40871')
fuzhi('40891')
fuzhi('40892')
fuzhi('40901')
fuzhi('40902')
fuzhi('40903')
fuzhi('40904')
fuzhi('40905')
fuzhi('40962')
fuzhi('40963')
fuzhi('40981')
fuzhi('40991')
fuzhi('40992')
fuzhi('41063')
fuzhi('41073')
fuzhi('63521')
fuzhi('63525')
fuzhi('63544')
fuzhi('63552')
fuzhi('63553')
fuzhi('63554')
fuzhi('63561')
fuzhi('63562')
fuzhi('63563')









