
void mergeBD()
{
file1 = new TFile("MT-D-Nominal.root");
file2 = new TFile("MT-B-Nominal.root");
file3 = new TFile("HT-D-Nominal.root");
file4 = new TFile("HT-B-Nominal.root");
cout << "opened" << endl;


hist411 = (TH1D*) file4->Get("MCQCD")->Clone("HT_QCD_B");
cout << hist411 << endl;
hist412 = (TH1D*) file4->Get("TTJets")->Clone("HT_TT_B");
hist413 = (TH1D*) file4->Get("WJets")->Clone("HT_W_B");
hist414 = (TH1D*) file4->Get("Data")->Clone("HT_data_B");
hist415 = (TH1D*) file4->Get("Tprime800_LH")->Clone("HT_Tprime800LH_B");
hist416 = (TH1D*) file4->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_B");
hist417 = (TH1D*) file4->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_B");
hist418 = (TH1D*) file4->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_B");

cout << "htb" << endl; 

hist211 = (TH1D*) file2->Get("MCQCD")->Clone("MTP_QCD_B");
hist212 = (TH1D*) file2->Get("TTJets")->Clone("MTP_TT_B");
hist213 = (TH1D*) file2->Get("WJets")->Clone("MTP_W_B");
hist214 = (TH1D*) file2->Get("Data")->Clone("MTP_data_B");
hist215 = (TH1D*) file2->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_B");
hist216 = (TH1D*) file2->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_B");
hist217 = (TH1D*) file2->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_B");
hist218 = (TH1D*) file2->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_B");
cout << "mtb" << endl; 

hist311 = (TH1D*) file3->Get("MCQCD")->Clone("HT_QCD_D");
hist312 = (TH1D*) file3->Get("TTJets")->Clone("HT_TT_D");
hist313 = (TH1D*) file3->Get("WJets")->Clone("HT_W_D");
hist315 = (TH1D*) file3->Get("Tprime800_LH")->Clone("HT_Tprime800LH_D");
hist316 = (TH1D*) file3->Get("Tprime1000_LH")->Clone("HT_Tprime1000LH_D");
hist317 = (TH1D*) file3->Get("Tprime1200_LH")->Clone("HT_Tprime1200LH_D");
hist318 = (TH1D*) file3->Get("Tprime1800_LH")->Clone("HT_Tprime1800LH_D");

cout << "htd" << endl; 
hist111 = (TH1D*) file1->Get("MCQCD")->Clone("MTP_QCD_D");
hist112 = (TH1D*) file1->Get("TTJets")->Clone("MTP_TT_D");
hist113 = (TH1D*) file1->Get("WJets")->Clone("MTP_W_D");
hist115 = (TH1D*) file1->Get("Tprime800_LH")->Clone("MTP_Tprime800LH_D");
hist116 = (TH1D*) file1->Get("Tprime1000_LH")->Clone("MTP_Tprime1000LH_D");
hist117 = (TH1D*) file1->Get("Tprime1200_LH")->Clone("MTP_Tprime1200LH_D");
hist118 = (TH1D*) file1->Get("Tprime1800_LH")->Clone("MTP_Tprime1800LH_D");
cout << "mtd" << endl; 

fileout = new TFile("RegionBD.root","RECREATE");
hist111->Write();
hist112->Write();
hist113->Write();
hist115->Write();
hist116->Write();
hist117->Write();
hist118->Write();

hist211->Write();
hist212->Write();
hist213->Write();
hist214->Write();
hist215->Write();
hist216->Write();
hist217->Write();
hist218->Write();

hist311->Write();
hist312->Write();
hist313->Write();
hist315->Write();
hist316->Write();
hist317->Write();
hist318->Write();

hist411->Write();
hist412->Write();
hist413->Write();
hist414->Write();
hist415->Write();
hist416->Write();
hist417->Write();
hist418->Write();

fileout->Close();
}
