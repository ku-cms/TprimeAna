import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_2.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_5.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_6.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_7.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_8.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_9.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_10.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_11.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_12.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_13.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_14.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_15.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_16.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_17.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_18.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_19.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_20.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_21.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_22.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_23.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Oct05-Presel/151103_202914/0000/PreselEvents_JetHT2015D-Oct05_24.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_2.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_5.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_6.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_7.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_8.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_9.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-Prompt-Presel/151103_202940/0000/PreselEvents_JetHT2015D-Prompt_10.root',
    )
)

