# xBuilder分析根目录
xBuilderSourceRoot = r"C:\xBuild\Source"
xBuilderPluginRoot = r"C:\xBuild\Plugins"
xBuilderRootdirs = [xBuilderSourceRoot, xBuilderPluginRoot]

# ignore plugins 目录
ignorePluginDir = [r"\BLUI", r"\ThirdParty"]
ignoreSourceDir = [r"\ThirdParty"]

# ignore path contain
ignorePathContain = [r'\Build', r'\Intermediate', r'\ThirdPartyWrapper']

# ignore .cpp
ignoreCppExt = ['.h.cpp', '.generated.cpp']

# ignore .h
ignoreHeaderExt = ['.generated.h', '.generated.dep.h', 'PCH.h']

# output dir
outputDir = r'\output'