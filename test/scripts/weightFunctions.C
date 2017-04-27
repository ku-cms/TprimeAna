#include "DataFormats/Math/interface/deltaR.h"
void weightFunctions(){
                   std::cout << "Weighting functions loaded." << endl;
                   return;
}

double topSFVal(double TopPT, int shift)
{


//   if( TopPT >= 400. && TopPT < 550.) {
//      if(shift == 0 ) return 1.37 ;
//      if(shift == 1 ) return 1.37+0.27 ;
//      if(shift == -1) return 1.37-0.27;
//    }
//    else if ( TopPT  >= 550.)  {
//      if(shift == 0 ) return 1.07 ;
//      if(shift == 1 ) return 1.07+0.34 ;
//      if(shift == -1) return 1.07-0.34;
//    }
   if( TopPT >= 400) {
        if(shift == 0) return 1.01;
        if(shift == 1) return 1.08;
        if(shift == -1) return 0.97;
     }
//   if( TopPT >= 400) {
//        if(shift == 0) return 1.05;
//        if(shift == 1) return 1.13;
//        if(shift == -1) return 1.01;
//     }
//   if( TopPT >= 400) {
//        if(shift == 0) return 1.05;
//        if(shift == 1) return 1.16;
//        if(shift == -1) return 1.00;
//     }
//   if( TopPT >= 400) {
//        if(shift == 0) return 1.08;
//        if(shift == 1) return 1.18;
//        if(shift == -1) return 1.04;
//     }
//   if( TopPT >= 400. && TopPT < 550.) {
//      if(shift == 0 ) return 0.88 ;
//      if(shift == 1 ) return 0.88+0.13 ;
//      if(shift == -1) return 0.88-0.13;
//    }
//    else if ( TopPT  >= 550.)  {
//      if(shift == 0 ) return 0.94 ;
//      if(shift == 1 ) return 0.94+0.29 ;
//      if(shift == -1) return 0.94-0.29;
//    }
        return 1;
}
double topSF(double TopPT)
{
        return topSFVal(TopPT,0);
}

double topSFUp(double TopPT)
{
        return topSFVal(TopPT,1);
}
double topSFDown(double TopPT)
{
        return topSFVal(TopPT,-1);
}

double WeightHT(double HT, int shift)
{

        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(0.000079 + (4.6073/100000000000*HT*HT) + (2*HT*-5.878/100000000)); //with b as intercept and m as slope 
                                                                                                       //Sqrt(sigma(b)^2 + sigma(m)^2*x^2 + 2*x*cov(m,b))
//        double wt = (1+((-0.000142726)*HT + 0.19121));
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 2700)
                return 1;

        return wt + (shift*sigErr) ; 

}
double QuadWeightHT(double HT, int shift)
{

//        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(2.96072e-9*2.96072e-9*HT*HT*HT*HT
                                  + 1.07286e-5*1.07286e-5*HT*HT 
                                  + 0.00921116*0.00921116
                                  + 2*HT*HT*HT*-3.1426e-14
                                  + 2*HT*HT*2.6219e-11
                                  + 2*HT*-9.7824e-8 );
        double wt = 3.82408e-8*HT*HT + -2.71605e-4*HT + 1.29308;
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 3200)
                return 1;

        return wt + (shift*sigErr) ; 

}

double dR(double eta1,double phi1, double eta2, double phi2) {

        return deltaR(eta1,phi1,eta2,phi2);
}

//TString Mjj(Int_t idx1, Int_t idx2){
 //   TString out;
//    out.Form("mass(ptAK8[idxAK8[%d]],etaAK8[idxAK8[%d]],phiAK8[idxAK8[%d]],MAK8[idxAK8[%d]],ptAK8[idxAK8[%d]],etaAK8[idxAK8[%d]],phiAK8[idxAK8[%d]],MAK8[idxAK8[%d]])",idx1,idx1,idx1,idx1,idx2,idx2,idx2,idx2);
//    return out;
//}

double Mjj(double pt1, double eta1, double phi1, double M1, double pt2, double eta2, double phi2, double M2){
    TLorentzVector V1, V2;
    V1.SetPtEtaPhiM(pt1,eta1,phi1,M1);
    V2.SetPtEtaPhiM(pt2,eta2,phi2,M2);
    return (V1+V2).M();
}
