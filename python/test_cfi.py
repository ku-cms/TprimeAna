import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/home/t3-ku/stringer/CMSSW_7_4_8_patch1/src/Analysis/Presel/test/PreselEvents_none.root',
    )
)

