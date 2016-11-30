#include "DataFormats/Math/interface/deltaR.h"
void weightFunctions(){
                   std::cout << "Weighting functions loaded." << endl;
                   return;
}

double topSFVal(double TopPT, int shift)
{


   if( TopPT >= 400. && TopPT < 550.) {
      if(shift == 0 ) return 1.37 ;
      if(shift == 1 ) return 1.37+0.27 ;
      if(shift == -1) return 1.37-0.27;
    }
    else if ( TopPT  >= 550.)  {
      if(shift == 0 ) return 1.07 ;
      if(shift == 1 ) return 1.07+0.34 ;
      if(shift == -1) return 1.07-0.34;
    }
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

//        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(0.000079 + (4.6073/100000000000*HT*HT) + (2*HT*-5.878/100000000));
        double wt = (1+((-0.000142726)*HT + 0.19121));
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 2700)
                return 1;

        return wt + (shift*sigErr) ; 

}
double QuadWeightHT(double HT, int shift)
{

//        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(0.000079 + (4.6073/100000000000*HT*HT) + (2*HT*-5.878/100000000));
        double wt = 3.82408e-8*HT*HT + -2.71605e-4*HT + 1.29308;
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 3200)
                return 1;

        return wt + (shift*sigErr) ; 

}

double dR(double eta1,double phi1, double eta2, double phi2) {

        return deltaR(eta1,phi1,eta2,phi2);
}
