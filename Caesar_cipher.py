
import string

# text = 'Hvs Pfwhwgv Rowzm Vsfozr ofhwqzs cb gc qozzsr gdmqzwghg vog fowgsr qcbqsfb oh ucjsfbasbh zsjszg hvoh hvs zofus ' \
#     'wbqfsogs wb hfojsz tfca hvs Qcbhwbsbh vog aogysr ob wbtwzhfohwcb cdsfohwcb pm hvs Opksvf. GWG vog fsqswjsr ' \
#     'fsdcfhghvoh Vwhzsf Mcihv ufcidg hfojszzwbu opfcor vojs pssb ogysr hc qcadzshs o rshowzsr eisghwcbbowfs, ' \
#     'wbqzirwbu eisghwcbg cb hsffowb, dcdizohwcb, obr dczwhwqoz jwskg ct hvs dcdizohwcb. JY vog hoysb o dsfgcboz ' \
#     'wbhsfsgh wb hvs ghcfm pih vwg fsgcifqsg ofs tizzm ozzcqohsr wb wbjsghwuohwbu o biapsf ct gigdsqhsr Usfaob ' \
#     'ousbhg ozfsorm zwjwbu wb hvs IY, gc PCGG vog pssb hogysr kwhv wbjsghwuohwbu obr fsdcfhwbu cb hvs gdmqzwgh ' \
#     'hcifwbu bshkcfy. Voffm wg qiffsbhzm sbuousr wbjsghwuohwbu Rws Ozqvsawghsb gc vs vog ogysr cif hsoa hc hoys ' \
#     'hvwg cb. Kvwzs wh wg dcggwpzs hvoh hvs qmqzs hcifwghg ofs cdsfohwbu og o tcfkofr cpgsfjsf rwjwgwcb wb ' \
#     'dfsdofohwcb tcf o tihifs wbjogwcb, hvs gaozz biapsfg wbjczjsr, obr hvswf hfojsz fcihsg aoys wh gssa zwyszm hvoh hvwg wg oh acgh o tswbh rsgwubsr hc rfok cif fsgcifqsg okom tfca acfs gwubwtwqobh cdsfohwcbg. Kvoh ks rc ybck wg hvoh hvsfs wg ob wbhszzwusbqs rwasbgwcb hc hvwg gwbqs cif cdsfohwjsg wb hvs UDC wbhsfqsdhsr hvs ohhoqvsr sbqfmdhsr asggous wb o pibrzs ct zshhsfg zsth dcghs fsghobhs tcf cbs ct hvs hcifwbu dofhwsg oh o Gqchhwgv dcgh cttwqs. Cif twfgh hogy wg hc rsqwdvsf hvwg asggous obr hc obozmgs whg qcbhsbhg. Sjsb wt hvwg hifbg cih hc ps o rwjsfgwcbofm hoqhwq wh dfcjwrsg ig kwhv ob cddcfhibwhm hc rsjszcd cif PCGG vcas wbhszzwusbqs cdsfohwcb obr ks kwzz ps hfsohwbu hvs awggwcb gsfwcigzm. Cdsfohwjsg tfca ozz hvfss PCGG rwjwgwcbg kwzz ps kcfywbu hcushvsf oh hvs Pfcorkom hc wbhsfqsdh, rsqwdvsf obr obozmgs dchsbhwozzm fszsjobh gcifqsg. Ks kwzz ps dcghwbu idrohsg vsfs wb hvs awggwcb dousg igwbu ghobrofr dfchcqczg. Gwbqs cif qcaaibwqohwcbg ofs dfchsqhsr ks kwzz, tcf bck, igs hwsf cbs (Qosgof obr ottwbs gvwth) sbqfmdhwcb. Mcif twszr wggis qwdvsf kvssz wg ohhoqvsr, obr mcif twfgh hogy wg hc rsqwdvsf hvs ohhoqvsr asggous obr hc ghirm wh qofstizzm. Dsofz.'

text = 'WKH HDVLHVW PHWKRG RI HQFLSKHULQJ D WHAW PHVVDJH LV WR ' \
       'UHSODFH HDFK OHWWHU EB DQRWKHU XVLQJ D ILAHG UXOH, VR IRU ' \
       'HADPSOH HYHUB OHWWHU D PDB EH UHSODFHG EB G, DQG HYHUB ' \
       'OHWWHU E EB WKH OHWWHU H DQG VR RQ.'

# text = 'HTSLWFYZQFYNTSX, DTZ FWJ STB FS JCUJWY FY GWJFPNSL YMJ HFJXFW HNUMJW, MFWWD'

alphabet = string.ascii_lowercase

for key in range(len(alphabet)):
    decoded_message = ''
    print(f'The key is {key}')
    for char in text:
        if char != ' ':
            idx = alphabet.find(char.lower())

            # Find the new decoded letter by moving the dictionary up a certain value of key
            new_idx = idx + key
            if new_idx >= len(alphabet):
                new_idx -= len(alphabet)
            decoded_letter = alphabet[new_idx]
        else:
            decoded_letter = ' '

        # Append to the whole text
        decoded_message += decoded_letter
    print(decoded_message)
