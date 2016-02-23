void fix(TH1D* in)
{
 int nbins = in->GetNbinsX();
 double value1 = in->GetBinContent(nbins+1);
 double value2 = in->GetBinContent(nbins);
 double err1 = in->GetBinError(nbins+1);
 double err2 = in->GetBinError(nbins);
 in->SetBinContent(nbins+1, 0);
 in->SetBinContent(nbins, value1 + value2);
 in->SetBinError(nbins, sqrt(err1*err1 + err2*err2));

 double value3 = in->GetBinContent(0);
 double value4 = in->GetBinContent(1);
 double err3 = in->GetBinError(0);
 double err4 = in->GetBinError(1);
 in->SetBinContent(0, 0);
 in->SetBinContent(1, value3 + value4);
 in->SetBinError(nbins, sqrt(err3*err3 + err4*err4));


}

void mergeNoHT()
{
cout << "start" << endl;
file1 = new TFile("NoHT/LimitHists-MTNominal.root");
//file2 = new TFile("NoHT/LimitHists-MTHTUp.root");
//file3 = new TFile("NoHT/LimitHists-MTHTDown.root");
file4 = new TFile("NoHT/LimitHists-MTlUp.root");
file5 = new TFile("NoHT/LimitHists-MTlDown.root");
file6 = new TFile("NoHT/LimitHists-MTbcUp.root");
file7 = new TFile("NoHT/LimitHists-MTbcDown.root");
file8 = new TFile("NoHT/LimitHists-MTttagUp.root");
file9 = new TFile("NoHT/LimitHists-MTttagDown.root");
file0 = new TFile("NoHT/JEC/LimitHists-MT_JERUp.root");
filea = new TFile("NoHT/JEC/LimitHists-MT_JERDown.root");
fileb = new TFile("NoHT/JEC/LimitHists-MT_JESUp.root");
filec = new TFile("NoHT/JEC/LimitHists-MT_JESDown.root");

file11 = new TFile("NoHT/LimitHists-HTNominal.root");
//file12 = new TFile("NoHT/LimitHists-HTHTUp.root");
//file13 = new TFile("NoHT/LimitHists-HTHTDown.root");
file14 = new TFile("NoHT/LimitHists-HTlUp.root");
file15 = new TFile("NoHT/LimitHists-HTlDown.root");
file16 = new TFile("NoHT/LimitHists-HTbcUp.root");
file17 = new TFile("NoHT/LimitHists-HTbcDown.root");
file18 = new TFile("NoHT/LimitHists-HTttagUp.root");
file19 = new TFile("NoHT/LimitHists-HTttagDown.root");
file10 = new TFile("NoHT/JEC/LimitHists-HT_JERUp.root");
file1a = new TFile("NoHT/JEC/LimitHists-HT_JERDown.root");
file1b = new TFile("NoHT/JEC/LimitHists-HT_JESUp.root");
file1c = new TFile("NoHT/JEC/LimitHists-HT_JESDown.root");

file21 = new TFile("SignalMT-Nominal.root");
//file22 = new TFile("SignalMT-HTUp.root");
//file23 = new TFile("SignalMT-HTDown.root");
file24 = new TFile("SignalMT-bcDown.root");
file25 = new TFile("SignalMT-bcUp.root");
file26 = new TFile("SignalMT-lDown.root");
file27 = new TFile("SignalMT-lUp.root");
file28 = new TFile("SignalMT-ttagDown.root");
file29 = new TFile("SignalMT-ttagUp.root");
file20 = new TFile("NoHT/JEC/SignalMT_JERUp.root");
file2a = new TFile("NoHT/JEC/SignalMT_JERDown.root");
file2b = new TFile("NoHT/JEC/SignalMT_JESUp.root");
file2c = new TFile("NoHT/JEC/SignalMT_JESDown.root");

file31 = new TFile("SignalHT-Nominal.root");
//file32 = new TFile("SignalHT-HTUp.root");
//file33 = new TFile("SignalHT-HTDown.root");
file34 = new TFile("SignalHT-btag_bcDown.root");
file35 = new TFile("SignalHT-btag_bcUp.root");
file36 = new TFile("SignalHT-btag_lDown.root");
file37 = new TFile("SignalHT-btag_lUp.root");
file38 = new TFile("SignalHT-ttagDown.root");
file39 = new TFile("SignalHT-ttagUp.root");
file30 = new TFile("NoHT/JEC/SignalHT_JERUp.root");
file3a = new TFile("NoHT/JEC/SignalHT_JERDown.root");
file3b = new TFile("NoHT/JEC/SignalHT_JESUp.root");
file3c = new TFile("NoHT/JEC/SignalHT_JESDown.root");
cout << "opened" << endl;

fileout = new TFile("LimitPlotsNoHT.root","RECREATE");

hist111 = (TH1D*) file11->Get("QCD-Est")->Clone("HT_QCD");
fix(hist111);
hist112 = (TH1D*) file11->Get("TT-MC")->Clone("HT_TT");
fix(hist112);
hist113 = (TH1D*) file11->Get("W-MC")->Clone("HT_W");
fix(hist113);

hist114 = (TH1D*) hist111->Clone("HT_background");
hist114->Add(hist112);
hist114->Add(hist113); 
/*
hist121 = (TH1D*) file12->Get("QCD-Est")->Clone("HT_QCD_HTUp");
fix(hist121);
hist122 = (TH1D*) file12->Get("TT-MC")->Clone("HT_TT_HTUp");
fix(hist122);
hist123 = (TH1D*) file12->Get("W-MC")->Clone("HT_W_HTUp");
fix(hist123);

hist124 = (TH1D*) hist121->Clone("HT_background_HTUp");
hist124->Add(hist122);
hist124->Add(hist123);


hist131 = (TH1D*) file13->Get("QCD-Est")->Clone("HT_QCD_HTDown");
fix(hist131);
hist132 = (TH1D*) file13->Get("TT-MC")->Clone("HT_TT_HTDown");
fix(hist132);
hist133 = (TH1D*) file13->Get("W-MC")->Clone("HT_W_HTDown");
fix(hist133);

hist134 = (TH1D*) hist131->Clone("HT_background_HTDown");
hist134->Add(hist132);
hist134->Add(hist133);
*/

hist161 = (TH1D*) file16->Get("QCD-Est")->Clone("HT_QCD_bcUp");
fix(hist161);
hist162 = (TH1D*) file16->Get("TT-MC")->Clone("HT_TT_bcUp");
fix(hist162);
hist163 = (TH1D*) file16->Get("W-MC")->Clone("HT_W_bcUp");
fix(hist163);

hist164 = (TH1D*) hist161->Clone("HT_background_bcUp");
hist164->Add(hist162);
hist164->Add(hist163);

hist171 = (TH1D*) file17->Get("QCD-Est")->Clone("HT_QCD_bcDown");
fix(hist171);
hist172 = (TH1D*) file17->Get("TT-MC")->Clone("HT_TT_bcDown");
fix(hist172);
hist173 = (TH1D*) file17->Get("W-MC")->Clone("HT_W_bcDown");
fix(hist173);

hist174 = (TH1D*) hist171->Clone("HT_background_bcDown");
hist174->Add(hist172);
hist174->Add(hist173);

hist141 = (TH1D*) file14->Get("QCD-Est")->Clone("HT_QCD_lUp");
fix(hist141);
hist142 = (TH1D*) file14->Get("TT-MC")->Clone("HT_TT_lUp");
fix(hist142);
hist143 = (TH1D*) file14->Get("W-MC")->Clone("HT_W_lUp");
fix(hist143);

hist144 = (TH1D*) hist141->Clone("HT_background_lUp");
hist144->Add(hist142);
hist144->Add(hist143);

hist151 = (TH1D*) file15->Get("QCD-Est")->Clone("HT_QCD_lDown");
fix(hist151);
hist152 = (TH1D*) file15->Get("TT-MC")->Clone("HT_TT_lDown");
fix(hist152);
hist153 = (TH1D*) file15->Get("W-MC")->Clone("HT_W_lDown");
fix(hist153);

hist154 = (TH1D*) hist151->Clone("HT_background_lDown");
hist154->Add(hist152);
hist154->Add(hist153);


hist181 = (TH1D*) file18->Get("QCD-Est")->Clone("HT_QCD_ttagUp");
fix(hist181);
hist182 = (TH1D*) file18->Get("TT-MC")->Clone("HT_TT_ttagUp");
fix(hist182);
hist183 = (TH1D*) file18->Get("W-MC")->Clone("HT_W_ttagUp");
fix(hist183);

hist184 = (TH1D*) hist181->Clone("HT_background_ttagUp");
hist184->Add(hist182);
hist184->Add(hist183);

hist191 = (TH1D*) file19->Get("QCD-Est")->Clone("HT_QCD_ttagDown");
fix(hist191);
hist192 = (TH1D*) file19->Get("TT-MC")->Clone("HT_TT_ttagDown");
fix(hist192);
hist193 = (TH1D*) file19->Get("W-MC")->Clone("HT_W_ttagDown");
fix(hist193);

hist194 = (TH1D*) hist191->Clone("HT_background_ttagDown");
hist194->Add(hist192);
hist194->Add(hist193);

hist101 = (TH1D*) file10->Get("QCD-Est")->Clone("HT_QCD_JERUp");
fix(hist101);
hist102 = (TH1D*) file10->Get("TT-MC")->Clone("HT_TT_JERUp");
fix(hist102);
hist103 = (TH1D*) file10->Get("W-MC")->Clone("HT_W_JERUp");
fix(hist103);

hist104 = (TH1D*) hist101->Clone("HT_background_JERUp");
hist104->Add(hist102);
hist104->Add(hist103);


hist1a1 = (TH1D*) file1a->Get("QCD-Est")->Clone("HT_QCD_JERDown");
fix(hist1a1);
hist1a2 = (TH1D*) file1a->Get("TT-MC")->Clone("HT_TT_JERDown");
fix(hist1a2);
hist1a3 = (TH1D*) file1a->Get("W-MC")->Clone("HT_W_JERDown");
fix(hist1a3);

hist1a4 = (TH1D*) hist1a1->Clone("HT_background_JERDown");
hist1a4->Add(hist1a2);
hist1a4->Add(hist1a3);


hist1b1 = (TH1D*) file1b->Get("QCD-Est")->Clone("HT_QCD_JESUp");
fix(hist1b1);
hist1b2 = (TH1D*) file1b->Get("TT-MC")->Clone("HT_TT_JESUp");
fix(hist1b2);
hist1b3 = (TH1D*) file1b->Get("W-MC")->Clone("HT_W_JESUp");
fix(hist1b3);

hist1b4 = (TH1D*) hist1b1->Clone("HT_background_JESUp");
hist1b4->Add(hist1b2);
hist1b4->Add(hist1b3);


hist1c1 = (TH1D*) file1c->Get("QCD-Est")->Clone("HT_QCD_JESDown");
fix(hist1c1);
hist1c2 = (TH1D*) file1c->Get("TT-MC")->Clone("HT_TT_JESDown");
fix(hist1c2);
hist1c3 = (TH1D*) file1c->Get("W-MC")->Clone("HT_W_JESDown");
fix(hist1c3);

hist1c4 = (TH1D*) hist1c1->Clone("HT_background_JESDown");
hist1c4->Add(hist1c2);
hist1c4->Add(hist1c3);


// Make stat err template

hist1d1 = (TH1D*) hist111->Clone("HT_QCD_StatUp");
hist1d2 = (TH1D*) hist112->Clone("HT_TT_StatUp");
hist1d3 = (TH1D*) hist113->Clone("HT_W_StatUp");
hist1d4 = (TH1D*) hist114->Clone("HT_background_StatUp");
hist1e1 = (TH1D*) hist111->Clone("HT_QCD_StatDown");
hist1e2 = (TH1D*) hist112->Clone("HT_TT_StatDown");
hist1e3 = (TH1D*) hist113->Clone("HT_W_StatDown");
hist1e4 = (TH1D*) hist114->Clone("HT_background_StatDown");

for(int i = 0 ; i <= 20 ; i++) {
        hist1d1->SetBinContent(i,hist1d1->GetBinContent(i)+hist1d1->GetBinError(i));
        hist1d2->SetBinContent(i,hist1d2->GetBinContent(i)+hist1d2->GetBinError(i));
        hist1d3->SetBinContent(i,hist1d3->GetBinContent(i)+hist1d3->GetBinError(i));
        hist1d4->SetBinContent(i,hist1d4->GetBinContent(i)+hist1d4->GetBinError(i));
        hist1e1->SetBinContent(i,hist1e1->GetBinContent(i)-hist1e1->GetBinError(i));
        hist1e2->SetBinContent(i,hist1e2->GetBinContent(i)-hist1e2->GetBinError(i));
        hist1e3->SetBinContent(i,hist1e3->GetBinContent(i)-hist1e3->GetBinError(i));
        hist1e4->SetBinContent(i,hist1e4->GetBinContent(i)-hist1e4->GetBinError(i));
}



cout << "Back1" <<endl;


hist11 = (TH1D*) file1->Get("QCD-Est")->Clone("MTP_QCD");
fix(hist11);
hist12 = (TH1D*) file1->Get("TT-MC")->Clone("MTP_TT");
fix(hist12);
hist13 = (TH1D*) file1->Get("W-MC")->Clone("MTP_W");
fix(hist13);

hist14 = (TH1D*) hist11->Clone("MTP_background");
hist14->Add(hist12);
hist14->Add(hist13); 
/*
hist21 = (TH1D*) file2->Get("QCD-Est")->Clone("MTP_QCD_HTUp");
fix(hist21);
hist22 = (TH1D*) file2->Get("TT-MC")->Clone("MTP_TT_HTUp");
fix(hist22);
hist23 = (TH1D*) file2->Get("W-MC")->Clone("MTP_W_HTUp");
fix(hist23);

hist24 = (TH1D*) hist21->Clone("MTP_background_HTUp");
hist24->Add(hist22);
hist24->Add(hist23);

hist31 = (TH1D*) file3->Get("QCD-Est")->Clone("MTP_QCD_HTDown");
fix(hist31);
hist32 = (TH1D*) file3->Get("TT-MC")->Clone("MTP_TT_HTDown");
fix(hist32);
hist33 = (TH1D*) file3->Get("W-MC")->Clone("MTP_W_HTDown");
fix(hist33);
hist34 = (TH1D*) hist31->Clone("MTP_background_HTDown");
hist34->Add(hist32);
hist34->Add(hist33);

*/
hist61 = (TH1D*) file6->Get("QCD-Est")->Clone("MTP_QCD_bcUp");
fix(hist61);
hist62 = (TH1D*) file6->Get("TT-MC")->Clone("MTP_TT_bcUp");
fix(hist62);
hist63 = (TH1D*) file6->Get("W-MC")->Clone("MTP_W_bcUp");
fix(hist63);

hist64 = (TH1D*) hist61->Clone("MTP_background_bcUp");
hist64->Add(hist62);
hist64->Add(hist63);

hist71 = (TH1D*) file7->Get("QCD-Est")->Clone("MTP_QCD_bcDown");
fix(hist71);
hist72 = (TH1D*) file7->Get("TT-MC")->Clone("MTP_TT_bcDown");
fix(hist72);
hist73 = (TH1D*) file7->Get("W-MC")->Clone("MTP_W_bcDown");
fix(hist73);

hist74 = (TH1D*) hist71->Clone("MTP_background_bcDown");
hist74->Add(hist72);
hist74->Add(hist73);

hist41 = (TH1D*) file4->Get("QCD-Est")->Clone("MTP_QCD_lUp");
fix(hist41);
hist42 = (TH1D*) file4->Get("TT-MC")->Clone("MTP_TT_lUp");
fix(hist42);
hist43 = (TH1D*) file4->Get("W-MC")->Clone("MTP_W_lUp");
fix(hist43);

hist44 = (TH1D*) hist41->Clone("MTP_background_lUp");
hist44->Add(hist42);
hist44->Add(hist43);

hist51 = (TH1D*) file5->Get("QCD-Est")->Clone("MTP_QCD_lDown");
fix(hist51);
hist52 = (TH1D*) file5->Get("TT-MC")->Clone("MTP_TT_lDown");
fix(hist52);
hist53 = (TH1D*) file5->Get("W-MC")->Clone("MTP_W_lDown");
fix(hist53);

hist54 = (TH1D*) hist51->Clone("MTP_background_lDown");
hist54->Add(hist52);
hist54->Add(hist53);

hist81 = (TH1D*) file8->Get("QCD-Est")->Clone("MTP_QCD_ttagUp");
fix(hist81);
hist82 = (TH1D*) file8->Get("TT-MC")->Clone("MTP_TT_ttagUp");
fix(hist82);
hist83 = (TH1D*) file8->Get("W-MC")->Clone("MTP_W_ttagUp");
fix(hist83);

hist84 = (TH1D*) hist81->Clone("MTP_background_ttagUp");
hist84->Add(hist82);
hist84->Add(hist83);

hist91 = (TH1D*) file9->Get("QCD-Est")->Clone("MTP_QCD_ttagDown");
fix(hist91);
hist92 = (TH1D*) file9->Get("TT-MC")->Clone("MTP_TT_ttagDown");
fix(hist92);
hist93 = (TH1D*) file9->Get("W-MC")->Clone("MTP_W_ttagDown");
fix(hist93);

hist94 = (TH1D*) hist91->Clone("MTP_background_ttagDown");
hist94->Add(hist92);
hist94->Add(hist93);
cout << "Back2" <<endl;

// Make stat err template

histd1 = (TH1D*) hist11->Clone("MTP_QCD_StatUp");
histd2 = (TH1D*) hist12->Clone("MTP_TT_StatUp");
histd3 = (TH1D*) hist13->Clone("MTP_W_StatUp");
histd4 = (TH1D*) hist14->Clone("MTP_background_StatUp");
histe1 = (TH1D*) hist11->Clone("MTP_QCD_StatDown");
histe2 = (TH1D*) hist12->Clone("MTP_TT_StatDown");
histe3 = (TH1D*) hist13->Clone("MTP_W_StatDown");
histe4 = (TH1D*) hist14->Clone("MTP_background_StatDown");

for(int i = 0 ; i <= 20 ; i++) {
        histd1->SetBinContent(i,histd1->GetBinContent(i)+histd1->GetBinError(i));
        histd2->SetBinContent(i,histd2->GetBinContent(i)+histd2->GetBinError(i));
        histd3->SetBinContent(i,histd3->GetBinContent(i)+histd3->GetBinError(i));
        histe1->SetBinContent(i,histe1->GetBinContent(i)-histe1->GetBinError(i));
        histe2->SetBinContent(i,histe2->GetBinContent(i)-histe2->GetBinError(i));
        histe3->SetBinContent(i,histe3->GetBinContent(i)-histe3->GetBinError(i));
}


hist01 = (TH1D*) file0->Get("QCD-Est")->Clone("MTP_QCD_JERUp");
fix(hist01);
hist02 = (TH1D*) file0->Get("TT-MC")->Clone("MTP_TT_JERUp");
fix(hist02);
hist03 = (TH1D*) file0->Get("W-MC")->Clone("MTP_W_JERUp");
fix(hist03);

hist04 = (TH1D*) hist01->Clone("MTP_background_JERUp");
hist04->Add(hist02);
hist04->Add(hist03);


hista1 = (TH1D*) filea->Get("QCD-Est")->Clone("MTP_QCD_JERDown");
fix(hista1);
hista2 = (TH1D*) filea->Get("TT-MC")->Clone("MTP_TT_JERDown");
fix(hista2);
hista3 = (TH1D*) filea->Get("W-MC")->Clone("MTP_W_JERDown");
fix(hista3);

hista4 = (TH1D*) hista1->Clone("MTP_background_JERDown");
hista4->Add(hista2);
hista4->Add(hista3);


histb1 = (TH1D*) fileb->Get("QCD-Est")->Clone("MTP_QCD_JESUp");
fix(histb1);
histb2 = (TH1D*) fileb->Get("TT-MC")->Clone("MTP_TT_JESUp");
fix(histb2);
histb3 = (TH1D*) fileb->Get("W-MC")->Clone("MTP_W_JESUp");
fix(histb3);

histb4 = (TH1D*) histb1->Clone("MTP_background_JESUp");
histb4->Add(histb2);
histb4->Add(histb3);

histc1 = (TH1D*) filec->Get("QCD-Est")->Clone("MTP_QCD_JESDown");
fix(histc1);
histc2 = (TH1D*) filec->Get("TT-MC")->Clone("MTP_TT_JESDown");
fix(hist02);
histc3 = (TH1D*) filec->Get("W-MC")->Clone("MTP_W_JESDown");
fix(histc3);

histc4 = (TH1D*) histc1->Clone("MTP_background_JESDown");
histc4->Add(histc2);
histc4->Add(histc3);


hist211 = (TH1D*) file21->Get("Tprime800_LH")->Clone("MTP_Tprime800LH");
fix(hist211);
hist212 = (TH1D*) file21->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH");
fix(hist212);
hist213 = (TH1D*) file21->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH");
fix(hist213);
hist214 = (TH1D*) file21->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH");
fix(hist214);

/*
hist221 = (TH1D*) file22->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_HTUp");
fix(hist221);
hist222 = (TH1D*) file22->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_HTUp");
fix(hist222);
hist223 = (TH1D*) file22->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_HTUp");
fix(hist223);
hist224 = (TH1D*) file22->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_HTUp");
fix(hist224);

hist231 = (TH1D*) file23->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_HTDown");
fix(hist231);
hist232 = (TH1D*) file23->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_HTDown");
fix(hist232);
hist233 = (TH1D*) file23->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_HTDown");
fix(hist233);
hist234 = (TH1D*) file23->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_HTDown");
fix(hist234);
*/

hist241 = (TH1D*) file24->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_bcDown");
fix(hist241);
hist242 = (TH1D*) file24->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_bcDown");
fix(hist242);
hist243 = (TH1D*) file24->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_bcDown");
fix(hist243);
hist244 = (TH1D*) file24->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_bcDown");
fix(hist244);

hist251 = (TH1D*) file25->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_bcUp");
fix(hist251);
hist252 = (TH1D*) file25->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_bcUp");
fix(hist252);
hist253 = (TH1D*) file25->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_bcUp");
fix(hist253);
hist254 = (TH1D*) file25->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_bcUp");
fix(hist254);

hist261 = (TH1D*) file26->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_lDown");
fix(hist261);
hist262 = (TH1D*) file26->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_lDown");
fix(hist262);
hist263 = (TH1D*) file26->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_lDown");
fix(hist263);
hist264 = (TH1D*) file26->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_lDown");
fix(hist264);

hist271 = (TH1D*) file27->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_lUp");
fix(hist271);
hist272 = (TH1D*) file27->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_lUp");
fix(hist272);
hist273 = (TH1D*) file27->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_lUp");
fix(hist273);
hist274 = (TH1D*) file27->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_lUp");
fix(hist274);

hist281 = (TH1D*) file28->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_ttagDown");
fix(hist281);
hist282 = (TH1D*) file28->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_ttagDown");
fix(hist262);
hist283 = (TH1D*) file28->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_ttagDown");
fix(hist283);
hist284 = (TH1D*) file28->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_ttagDown");
fix(hist284);

hist291 = (TH1D*) file29->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_ttagUp");
fix(hist291);
hist292 = (TH1D*) file29->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_ttagUp");
fix(hist292);
hist293 = (TH1D*) file29->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_ttagUp");
fix(hist293);
hist294 = (TH1D*) file29->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_ttagUp");
fix(hist294);

hist201 = (TH1D*) file20->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_JERUp");
fix(hist201);
hist202 = (TH1D*) file20->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_JERUp");
fix(hist202);
hist203 = (TH1D*) file20->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_JERUp");
fix(hist203);
hist204 = (TH1D*) file20->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_JERUp");
fix(hist204);

hist2a1 = (TH1D*) file2a->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_JERDown");
fix(hist2a1);
hist2a2 = (TH1D*) file2a->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_JERDown");
fix(hist2a2);
hist2a3 = (TH1D*) file2a->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_JERDown");
fix(hist2a3);
hist2a4 = (TH1D*) file2a->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_JERDown");
fix(hist2a4);

hist2b1 = (TH1D*) file2b->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_JESUp");
fix(hist2b1);
hist2b2 = (TH1D*) file2b->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_JESUp");
fix(hist2b2);
hist2b3 = (TH1D*) file2b->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_JESUp");
fix(hist2b3);
hist2b4 = (TH1D*) file2b->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_JESUp");
fix(hist2b4);

hist2c1 = (TH1D*) file2c->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_JESDown");
fix(hist2c1);
hist2c2 = (TH1D*) file2c->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_JESDown");
fix(hist2c2);
hist2c3 = (TH1D*) file2c->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_JESDown");
fix(hist2c3);
hist2c4 = (TH1D*) file2c->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_JESDown");
fix(hist2c4);
// Make stat err template

hist2d1 = (TH1D*) hist211->Clone("MTP_Tprime800LH_StatUp"); 
hist2d2 = (TH1D*) hist212->Clone("MTP_Tprime1000LH_StatUp"); 
hist2d3 = (TH1D*) hist213->Clone("MTP_Tprime1200LH_StatUp"); 
hist2d4 = (TH1D*) hist214->Clone("MTP_Tprime1800LH_StatUp"); 
hist2e1 = (TH1D*) hist211->Clone("MTP_Tprime800LH_StatDown"); 
hist2e2 = (TH1D*) hist212->Clone("MTP_Tprime1000LH_StatDown"); 
hist2e3 = (TH1D*) hist213->Clone("MTP_Tprime1200LH_StatDown"); 
hist2e4 = (TH1D*) hist214->Clone("MTP_Tprime1800LH_StatDown"); 

for(int i = 0 ; i <= 20 ; i++) {
	hist2d1->SetBinContent(i,hist2d1->GetBinContent(i)+hist2d1->GetBinError(i));
	hist2d2->SetBinContent(i,hist2d2->GetBinContent(i)+hist2d2->GetBinError(i));
	hist2d3->SetBinContent(i,hist2d3->GetBinContent(i)+hist2d3->GetBinError(i));
	hist2d4->SetBinContent(i,hist2d4->GetBinContent(i)+hist2d4->GetBinError(i));
	hist2e1->SetBinContent(i,hist2e1->GetBinContent(i)-hist2e1->GetBinError(i));
	hist2e2->SetBinContent(i,hist2e2->GetBinContent(i)-hist2e2->GetBinError(i));
	hist2e3->SetBinContent(i,hist2e3->GetBinContent(i)-hist2e3->GetBinError(i));
	hist2e4->SetBinContent(i,hist2e4->GetBinContent(i)-hist2e4->GetBinError(i));
}


cout << "Signal1" <<endl;

hist311 = (TH1D*) file31->Get("Tprime800_LH")->Clone("HT_Tprime800LH");
fix(hist311);
hist312 = (TH1D*) file31->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH");
fix(hist312);
hist313 = (TH1D*) file31->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH");
fix(hist313);
hist314 = (TH1D*) file31->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH");
fix(hist314);

/*
hist321 = (TH1D*) file32->Get("Tprime800_LH")->Clone("HT_Tprime800LH_HTUp");
fix(hist321);
hist322 = (TH1D*) file32->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_HTUp");
fix(hist322);
hist323 = (TH1D*) file32->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_HTUp");
fix(hist323);
hist324 = (TH1D*) file32->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_HTUp");
fix(hist324);

hist331 = (TH1D*) file33->Get("Tprime800_LH")->Clone("HT_Tprime800LH_HTDown");
fix(hist331);
hist332 = (TH1D*) file33->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_HTDown");
fix(hist332);
hist333 = (TH1D*) file33->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_HTDown");
fix(hist333);
hist334 = (TH1D*) file33->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_HTDown");
fix(hist334);
*/

hist341 = (TH1D*) file34->Get("Tprime800_LH")->Clone("HT_Tprime800LH_bcDown");
fix(hist341);
hist342 = (TH1D*) file34->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_bcDown");
fix(hist342);
hist343 = (TH1D*) file34->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_bcDown");
fix(hist343);
hist344 = (TH1D*) file34->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_bcDown");
fix(hist344);

hist351 = (TH1D*) file35->Get("Tprime800_LH")->Clone("HT_Tprime800LH_bcUp");
fix(hist351);
hist352 = (TH1D*) file35->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_bcUp");
fix(hist352);
hist353 = (TH1D*) file35->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_bcUp");
fix(hist353);
hist354 = (TH1D*) file35->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_bcUp");
fix(hist354);

hist361 = (TH1D*) file36->Get("Tprime800_LH")->Clone("HT_Tprime800LH_lDown");
fix(hist361);
hist362 = (TH1D*) file36->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_lDown");
fix(hist362);
hist363 = (TH1D*) file36->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_lDown");
fix(hist363);
hist364 = (TH1D*) file36->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_lDown");
fix(hist364);

hist371 = (TH1D*) file37->Get("Tprime800_LH")->Clone("HT_Tprime800LH_lUp");
fix(hist371);
hist372 = (TH1D*) file37->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_lUp");
fix(hist372);
hist373 = (TH1D*) file37->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_lUp");
fix(hist373);
hist374 = (TH1D*) file37->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_lUp");
fix(hist374);

hist381 = (TH1D*) file38->Get("Tprime800_LH")->Clone("HT_Tprime800LH_ttagDown");
fix(hist381);
hist382 = (TH1D*) file38->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_ttagDown");
fix(hist362);
hist383 = (TH1D*) file38->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_ttagDown");
fix(hist383);
hist384 = (TH1D*) file38->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_ttagDown");
fix(hist384);

hist391 = (TH1D*) file39->Get("Tprime800_LH")->Clone("HT_Tprime800LH_ttagUp");
fix(hist391);
hist392 = (TH1D*) file39->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_ttagUp");
fix(hist392);
hist393 = (TH1D*) file39->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_ttagUp");
fix(hist393);
hist394 = (TH1D*) file39->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_ttagUp");
fix(hist394);

hist301 = (TH1D*) file30->Get("Tprime800_LH")->Clone("HT_Tprime800LH_JERUp");
fix(hist301);
hist302 = (TH1D*) file30->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_JERUp");
fix(hist302);
hist303 = (TH1D*) file30->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_JERUp");
fix(hist303);
hist304 = (TH1D*) file30->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_JERUp");
fix(hist304);

hist3a1 = (TH1D*) file3a->Get("Tprime800_LH")->Clone("HT_Tprime800LH_JERDown");
fix(hist3a1);
hist3a2 = (TH1D*) file3a->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_JERDown");
fix(hist3a2);
hist3a3 = (TH1D*) file3a->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_JERDown");
fix(hist3a3);
hist3a4 = (TH1D*) file3a->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_JERDown");
fix(hist3a4);

hist3b1 = (TH1D*) file3b->Get("Tprime800_LH")->Clone("HT_Tprime800LH_JESUp");
fix(hist3b1);
hist3b2 = (TH1D*) file3b->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_JESUp");
fix(hist3b2);
hist3b3 = (TH1D*) file3b->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_JESUp");
fix(hist3b3);
hist3b4 = (TH1D*) file3b->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_JESUp");
fix(hist3b4);

hist3c1 = (TH1D*) file3c->Get("Tprime800_LH")->Clone("HT_Tprime800LH_JESDown");
fix(hist3c1);
hist3c2 = (TH1D*) file3c->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_JESDown");
fix(hist3c2);
hist3c3 = (TH1D*) file3c->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_JESDown");
fix(hist3c3);
hist3c4 = (TH1D*) file3c->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_JESDown");
fix(hist3c4);

cout << "Signal2" <<endl;

hist3d1 = (TH1D*) hist311->Clone("HT_Tprime800LH_StatUp");
hist3d2 = (TH1D*) hist312->Clone("HT_Tprime1000LH_StatUp");
hist3d3 = (TH1D*) hist313->Clone("HT_Tprime1200LH_StatUp");
hist3d4 = (TH1D*) hist314->Clone("HT_Tprime1800LH_StatUp");
hist3e1 = (TH1D*) hist311->Clone("HT_Tprime800LH_StatDown");
hist3e2 = (TH1D*) hist312->Clone("HT_Tprime1000LH_StatDown");
hist3e3 = (TH1D*) hist313->Clone("HT_Tprime1200LH_StatDown");
hist3e4 = (TH1D*) hist314->Clone("HT_Tprime1800LH_StatDown");

for(int i = 0 ; i <= 36 ; i++) {
        hist3d1->SetBinContent(i,hist3d1->GetBinContent(i)+hist3d1->GetBinError(i));
        hist3d2->SetBinContent(i,hist3d2->GetBinContent(i)+hist3d2->GetBinError(i));
        hist3d3->SetBinContent(i,hist3d3->GetBinContent(i)+hist3d3->GetBinError(i));
        hist3d4->SetBinContent(i,hist3d4->GetBinContent(i)+hist3d4->GetBinError(i));
        hist3e1->SetBinContent(i,hist3e1->GetBinContent(i)-hist3e1->GetBinError(i));
        hist3e2->SetBinContent(i,hist3e2->GetBinContent(i)-hist3e2->GetBinError(i));
        hist3e3->SetBinContent(i,hist3e3->GetBinContent(i)-hist3e3->GetBinError(i));
        hist3e4->SetBinContent(i,hist3e4->GetBinContent(i)-hist3e4->GetBinError(i));
}


histHT = (TH1D*) file11->Get("data_obs")->Clone("HT_data_obs");
fix(histHT);
histMT = (TH1D*) file1->Get("data_obs")->Clone("MTP_data_obs");
fix(histMT);


fileout->cd();
hist11->Write();
hist12->Write();
hist13->Write();
hist14->Write();
/*
hist21->Write();
hist22->Write();
hist23->Write();
hist24->Write();
hist31->Write();
hist32->Write();
hist33->Write();
hist34->Write();

*/
hist41->Write();
hist42->Write();
hist43->Write();
hist44->Write();
hist51->Write();
hist52->Write();
hist53->Write();
hist54->Write();
hist61->Write();
hist62->Write();
hist63->Write();
hist64->Write();
hist71->Write();
hist72->Write();
hist73->Write();
hist74->Write();
hist81->Write();
hist82->Write();
hist83->Write();
hist84->Write();
hist91->Write();
hist92->Write();
hist93->Write();
hist94->Write();
hist01->Write();
hist02->Write();
hist03->Write();
hist04->Write();
hista1->Write();
hista2->Write();
hista3->Write();
hista4->Write();
histb1->Write();
histb2->Write();
histb3->Write();
histb4->Write();
histc1->Write();
histc2->Write();
histc3->Write();
histc4->Write();
histd1->Write();
histd2->Write();
histd3->Write();
histd4->Write();
histe1->Write();
histe2->Write();
histe3->Write();
histe4->Write();
hist111->Write();
hist112->Write();
hist113->Write();
hist114->Write();
/*hist121->Write();
hist122->Write();
hist123->Write();
hist124->Write();
hist131->Write();
hist132->Write();
hist133->Write();
hist134->Write();
*/
hist141->Write();
hist142->Write();
hist143->Write();
hist144->Write();
hist151->Write();
hist152->Write();
hist153->Write();
hist154->Write();
hist161->Write();
hist162->Write();
hist163->Write();
hist164->Write();
hist171->Write();
hist172->Write();
hist173->Write();
hist174->Write();
hist181->Write();
hist182->Write();
hist183->Write();
hist184->Write();
hist191->Write();
hist192->Write();
hist193->Write();
hist194->Write();
hist101->Write();
hist102->Write();
hist103->Write();
hist104->Write();
hist1a1->Write();
hist1a2->Write();
hist1a3->Write();
hist1a4->Write();
hist1b1->Write();
hist1b2->Write();
hist1b3->Write();
hist1b4->Write();
hist1c1->Write();
hist1c2->Write();
hist1c3->Write();
hist1c4->Write();
hist1d1->Write();
hist1d2->Write();
hist1d3->Write();
hist1d4->Write();
hist1e1->Write();
hist1e2->Write();
hist1e3->Write();
hist1e4->Write();
hist211->Write();
hist212->Write();
hist213->Write();
hist214->Write();
/*hist221->Write();
hist222->Write();
hist223->Write();
hist224->Write();
hist231->Write();
hist232->Write();
hist233->Write();
hist234->Write();
*/
hist241->Write();
hist242->Write();
hist243->Write();
hist244->Write();
hist251->Write();
hist252->Write();
hist253->Write();
hist254->Write();
hist261->Write();
hist262->Write();
hist263->Write();
hist264->Write();
hist271->Write();
hist272->Write();
hist273->Write();
hist274->Write();
hist281->Write();
hist282->Write();
hist283->Write();
hist284->Write();
hist291->Write();
hist292->Write();
hist293->Write();
hist294->Write();
hist201->Write();
hist202->Write();
hist203->Write();
hist204->Write();
hist2a1->Write();
hist2a2->Write();
hist2a3->Write();
hist2a4->Write();
hist2b1->Write();
hist2b2->Write();
hist2b3->Write();
hist2b4->Write();
hist2c1->Write();
hist2c2->Write();
hist2c3->Write();
hist2c4->Write();
hist2d1->Write();
hist2d2->Write();
hist2d3->Write();
hist2d4->Write();
hist2e1->Write();
hist2e2->Write();
hist2e3->Write();
hist2e4->Write();
hist311->Write();
hist312->Write();
hist313->Write();
hist314->Write();
/*hist321->Write();
hist322->Write();
hist323->Write();
hist324->Write();
hist331->Write();
hist332->Write();
hist333->Write();
hist334->Write();
*/
hist341->Write();
hist342->Write();
hist343->Write();
hist344->Write();
hist351->Write();
hist352->Write();
hist353->Write();
hist354->Write();
hist361->Write();
hist362->Write();
hist363->Write();
hist364->Write();
hist371->Write();
hist372->Write();
hist373->Write();
hist374->Write();
hist381->Write();
hist382->Write();
hist383->Write();
hist384->Write();
hist391->Write();
hist392->Write();
hist393->Write();
hist394->Write();
hist301->Write();
hist302->Write();
hist303->Write();
hist304->Write();
hist3a1->Write();
hist3a2->Write();
hist3a3->Write();
hist3a4->Write();
hist3b1->Write();
hist3b2->Write();
hist3b3->Write();
hist3b4->Write();
hist3c1->Write();
hist3c2->Write();
hist3c3->Write();
hist3c4->Write();
hist3d1->Write();
hist3d2->Write();
hist3d3->Write();
hist3d4->Write();
hist3e1->Write();
hist3e2->Write();
hist3e3->Write();
hist3e4->Write();

histHT->SetBinError(20,0);

histHT->Write();
histMT->Write();

}
