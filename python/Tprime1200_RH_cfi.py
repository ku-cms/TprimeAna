import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TprimeBToTH_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_TPrime1200_RH/151103_045610/0000/PreselEvents_TPrime1200_RH_1.root',
    )
)

