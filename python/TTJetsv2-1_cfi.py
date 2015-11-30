import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_2.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_5.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_6.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_7.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_8.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_9.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_10.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_11.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_12.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_13.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_14.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_15.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_16.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_17.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_18.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_19.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_20.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_21.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/TT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTJetsv2/151104_001102/0000/PreselEvents_TTJetsv2_22.root',
    ),
    #skipEvents = cms.untracked.uint32(511001)
)

