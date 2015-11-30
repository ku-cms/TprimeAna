import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_2.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_5.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_6.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_7.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_8.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_9.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_10.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_11.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_12.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_13.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_14.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_15.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_16.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_17.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_18.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_19.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_20.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_21.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_22.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_23.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_24.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_25.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_26.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_27.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_28.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_29.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_30.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_31.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_32.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_33.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_34.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_35.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_36.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_37.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_38.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_39.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_40.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_41.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_42.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_43.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_44.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_45.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_46.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_47.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_48.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_49.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_50.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_51.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_52.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_ttbar/151120_044554/0000/PreselEvents_ttbar_53.root',
    ),
    #skipEvents = cms.untracked.uint32(511001)
)

