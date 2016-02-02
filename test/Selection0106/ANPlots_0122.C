#include "TROOT.h"
#include "TSystem.h"
#include "TCanvas.h"



void ANPlots(TString outpath)
{


gSystem->Load("makeStack4_C.so");
TCanvas * c1;
TPad * p1;

// Presel plots -- No HT

/* 
makeStack("@AK8Idx.size()","htak4>1000","Tprime1200_LH","nAK8s","Jets","Number of AK8Jets",1000,1,5,0,5,"EvtWeight[0]*EvtWeight[4]/1.21");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"nak8_presel.pdf");

makeStack("@AK4Idx.size()","htak4>1000","Tprime1200_LH","# AK4 Jets","Events","Number of AK4 Jets",1000,1,10,0,10,"EvtWeight[0]*EvtWeight[4]/1.21");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"nak4.pdf");


makeStack("ptAK4[AK4Idx]","htak4>1000","Tprime1200_LH","p_{T} AK4 Jets","Jets","p_{T} of AK4 Jets ",1000,1,34,30,710,"EvtWeight[0]*EvtWeight[4]/1.21");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"ptak4.pdf");

makeStack("etaAK4[AK4Idx]","htak4>1000","Tprime1200_LH","#eta","Jets","#eta AK4 Jets",1000,1,50,-5,5,"EvtWeight[0]*EvtWeight[4]/1.21");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"etaak4.pdf");

makeStack("etaAK8[AK8Idx[0]]","htak4>1000","Tprime1200_LH","#eta","Jets","#eta Leading AK8 Jet",1000,1,50,-5,5,"EvtWeight[0]*EvtWeight[4]/1.21");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"etaak8leading.pdf");


// Presel plots -- HT Corrected


makeStack("etaAK8[AK8Idx[0]]","htak4>1000","Tprime1200_LH","#eta","Jets","#eta Leading AK8 Jet",1000,1,50,-5,5,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"etaak8leading_htcorr.pdf");



makeStack("etaAK4[AK4Idx]","htak4>1000","Tprime1200_LH","#eta","Jets","#eta AK4 Jets",1000,1,50,-5,5,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"etaak4_htcorr.pdf");



makeStack("ptAK4[AK4Idx[0]]","htak4>1000","Tprime1200_LH","p_{T} AK4 Jets","Jets/ 50 GeV","p_{T} of Leading AK4 Jets ",1000,1,36,300,2100,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"ptak4htcorrleading.pdf");


makeStack("ptAK8[AK8Idx[0]]","htak4>1000","Tprime1200_LH","p_{T} AK8 Jets","Jets/ 50 GeV","p_{T} of Leading AK8 Jets ",1000,1,36,300,2100,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"ptak8htcorrleading.pdf");

makeStack("@AK8Idx.size()","htak4>1000","Tprime1200_LH","nAK8s","Jets","Number of AK8Jets",1,1,5,0,5,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"nak8htcorr_presel.pdf");

makeStack("@AK4Idx.size()","htak4>1000","Tprime1200_LH","# AK4 Jets","Events","Number of AK4 Jets",1,1,10,0,10,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"nak4htcorr.pdf");

makeStack("ptAK4[AK4Idx]","htak4>1000","Tprime1200_LH","p_{T} AK4 Jets","Jets","p_{T} of AK4 Jets ",1000,1,34,30,710,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"ptak4htcorr.pdf");


makeStack("SoftDropMassAK8[AK8Idx]","htak4>1000&&subjAK8[AK8Idx]==3","Tprime1200_LH","SoftDropMass (GeV)","Jets","SoftDropMass AK8 Jets (3 subjets)",1,1,40,0,800,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"sdtopmass.pdf");

makeStack("PrunedMassAK8[AK8Idx]","htak4>1000&&subjAK8[AK8Idx]==2","Tprime1200_LH","PrunedMass (GeV)","Jets","PrunedMass AK8 Jets (2 subjets)",1,1,40,0,800,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"mprunehiggs.pdf");


makeStack("tau2AK8[AK8Idx]/tau1AK8[AK8Idx]","htak4>1000&&subjAK8[AK8Idx]==2","Tprime1200_LH","#tau_{21}","Jets","#tau_{21} AK8 Jets (2 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"tau21.pdf");

makeStack("tau3AK8[AK8Idx]/tau2AK8[AK8Idx]","htak4>1000&&subjAK8[AK8Idx]==3","Tprime1200_LH","#tau_{32}","Jets","#tau_{32} AK8 Jets (3 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"tau32.pdf");


makeStack("sjCSVAK8[sj0IdxAK8[AK8Idx]]","htak4>1000&&subjAK8[AK8Idx]==2&&sj0IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Subjet 0 CSV AK8 Jets (2 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv2h0.pdf");



makeStack("sjCSVAK8[sj1IdxAK8[AK8Idx]]","htak4>1000&&subjAK8[AK8Idx]==2&&sj1IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Subjet 1 CSV AK8 Jets (2 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv2h1.pdf");


makeStack("max(sjCSVAK8[sj0IdxAK8[AK8Idx]],sjCSVAK8[sj1IdxAK8[AK8Idx]])","htak4>1000&&subjAK8[AK8Idx]==2&&sj0IdxAK8[AK8Idx]>=0&&sj1IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Max Subjet CSV AK8 Jets (2 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv1sth.pdf");
*/

makeStack("min(sjCSVAK8[sj0IdxAK8[AK8Idx]],sjCSVAK8[sj1IdxAK8[AK8Idx]])","htak4>1000&&subjAK8[AK8Idx]==2&&sj0IdxAK8[AK8Idx]>=0&&sj1IdxAK8[AK8Idx]>=0&&(sjCSVAK8[sj0IdxAK8[AK8Idx]]>0.605||sjCSVAK8[sj1IdxAK8[AK8Idx]]>0.605)","Tprime1200_LH","subjet CSV","Jets","Max Subjet CSV AK8 Jets (2 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv2ndh.pdf");


makeStack("sjCSVAK8[sj0IdxAK8[AK8Idx]]","htak4>1000&&subjAK8[AK8Idx]==3&&sj0IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Subjet 0 CSV AK8 Jets (3 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv3t0.pdf");

h0QCD = (TH1D*) gROOT->FindObject("histQCD");
h0W = (TH1D*) gROOT->FindObject("ht11");
h0TT = (TH1D*) gROOT->FindObject("ht2");
h0data = (TH1D*) gROOT->FindObject("htdata");
h0sig = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h0back =  (TH1D*) gROOT->FindObject("hBack");


makeStack("sjCSVAK8[sj1IdxAK8[AK8Idx]]","htak4>1000&&subjAK8[AK8Idx]==3&&sj1IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Subjet 1 CSV AK8 Jets (3 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv3t1.pdf");

h1QCD = (TH1D*) gROOT->FindObject("histQCD");
h1W = (TH1D*) gROOT->FindObject("ht11");
h1TT = (TH1D*) gROOT->FindObject("ht2");
h1data = (TH1D*) gROOT->FindObject("htdata");
h1sig = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h1back =  (TH1D*) gROOT->FindObject("hBack");

makeStack("sjCSVAK8[sj0IdxAK8[AK8Idx]]","htak4>1000&&subjAK8[AK8Idx]==3&&sj2IdxAK8[AK8Idx]>=0","Tprime1200_LH","subjet CSV","Jets","Subjet 2 CSV AK8 Jets (3 subjets)",1000,1,50,0,1,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"csv3t2.pdf");

h2QCD = (TH1D*) gROOT->FindObject("histQCD");
h2W = (TH1D*) gROOT->FindObject("ht11");
h2TT = (TH1D*) gROOT->FindObject("ht2");
h2data = (TH1D*) gROOT->FindObject("htdata");
h2sig = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h2back =  (TH1D*) gROOT->FindObject("hBack");

h0QCD->Add(h1QCD);
h0QCD->Add(h2QCD);

h0W->Add(h1W);
h0W->Add(h2W);

h0TT->Add(h1TT);
h0TT->Add(h2TT);

h0data->Add(h1data);
h0data->Add(h2data);

h0sig->Add(h1sig);
h0sig->Add(h2sig);

h0back->Add(h1back);
h0back->Add(h2back);

map<TH1D*,TString> sig;
sig.insert(make_pair(h0sig,"Tprime1200_LH"));

c1->Clear();

DrawPlot(c1, h0back, h0data, sig, h0QCD ,h0W , h0TT);
c1->Print(outpath+"csv3t.pdf");


makeStack("@HTagIdx.size()","htak4>1000","Tprime1200_LH","nHTags","Events","Number of HTags",1,1,5,0,5,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
c1 = (TCanvas * ) gROOT->FindObject("c1");
p1 = (TPad * ) gROOT->FindObject("pad1");
p1->SetLogy();
c1->Print(outpath+"nhtags-htcorr.pdf");


makeStack("htak4","htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0","Tprime1200_LH","H_{T} GeV","Events/80 GeV","",1,1,20,1000,2600,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)",false,false);
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"htcuts.pdf");

makeStack("mass(ptAK8[HTagIdx[0]],etaAK8[HTagIdx[0]],phiAK8[HTagIdx[0]],MAK8[HTagIdx[0]],ptAK8[TTagIdx03[0]],etaAK8[TTagIdx03[0]],phiAK8[TTagIdx03[0]],MAK8[TTagIdx03[0]])","htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0","Tprime1200_LH", "M_{T} GeV", "Events/50 GeV", "" , 1,1, 20, 600,2400,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)",false,false);
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Print(outpath+"mtcuts.pdf");


makeStack("mass(ptAK8[HTagIdx[0]],etaAK8[HTagIdx[0]],phiAK8[HTagIdx[0]],MAK8[HTagIdx[0]],ptAK8[TTagIdx03[0]],etaAK8[TTagIdx03[0]],phiAK8[TTagIdx03[0]],MAK8[TTagIdx03[0]])","htak4>1000&&@HTagIdx.size()>0&&TTagIdx03.size()>0","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "M_{T} GeV", "Events/50 GeV", "" , 1,1, 36, 600,2400,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

hSig1 = (TH1D*) gROOT->FindObject("Tprime1000_LH");
hSig2 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
hSig3 = (TH1D*) gROOT->FindObject("Tprime1500_LH");
hSig4 = (TH1D*) gROOT->FindObject("Tprime1800_LH");

map<TH1D*,TString> signals;

signals.insert(make_pair(hSig1,TString("Tprime1000_LH")));
signals.insert(make_pair(hSig2,TString("Tprime1200_LH")));
signals.insert(make_pair(hSig3,TString("Tprime1500_LH")));
signals.insert(make_pair(hSig4,TString("Tprime1800_LH")));

DrawPlot(c1,0,0,signals);
c1->Print("mtsigcuts.pdf");
c1->SaveAs("mtsigcuts.C");


makeStack("htak4","htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "H_{T} GeV", "Events/50 GeV", "" , 1,1, 20, 1000,2600,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

c1 = (TCanvas * ) gROOT->FindObject("c1");
hSig1 = (TH1D*) gROOT->FindObject("Tprime1000_LH");
hSig2 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
hSig3 = (TH1D*) gROOT->FindObject("Tprime1500_LH");
hSig4 = (TH1D*) gROOT->FindObject("Tprime1800_LH");

map<TH1D*,TString> signals2;

signals2.insert(make_pair(hSig1,TString("Tprime1000_LH")));
signals2.insert(make_pair(hSig2,TString("Tprime1200_LH")));
signals2.insert(make_pair(hSig3,TString("Tprime1500_LH")));
signals2.insert(make_pair(hSig4,TString("Tprime1800_LH")));

c1->Clear();

DrawPlot(c1,0,0,signals2);
c1->Print("htsigcuts.pdf");
c1->SaveAs("htsigcuts.C");

ABCDData(0);
h1 = (TH1D*) gROOT->FindObject("DestMC");
h1->SaveAs("Ht-EstMC.root");
h2 = (TH1D*) gROOT->FindObject("Dest");
h2->SaveAs("Ht-EstData.root");

ABCDData(1);
h1 = (TH1D*) gROOT->FindObject("DestMC");
h1->SaveAs("Mt-EstMC.root");
h2 = (TH1D*) gROOT->FindObject("Dest");
h2->SaveAs("Mt-EstData.root");



}

