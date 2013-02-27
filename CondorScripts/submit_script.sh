#GetEnv = True
#executable =  /afs/csail.mit.edu/system/common/matlab/2010a/bin/matlab
#executable =  /afs/csail.mit.edu/common/matlab/2010a/bin/matlab
#executable =  /data/zfs-scratch/matlab-2012a/bin/matlab
executable = /usr/bin/python
universe = vanilla
priority = 0
Notification = Never
# yodel machines have no scipy

# 2GB MEMORY REQUIREMENT
requirements = OpSys == "LINUX" && Memory >= 2048

#Requirements = Machine != "yodel7.csail.mit.edu" && Machine != "yodel4.csail.mit.edu" && Machine != "yodel2.csail.mit.edu" && Machine !=
#Requirements = isPublic && \
#               Memory >= 6144 && \
#               Cpus >= 1 && \
#Requirements = Arch == "X86_64"

Error = CondorOutput/err/$(PROCESS).err
Log = CondorOutput/log/$(PROCESS).log
Output = CondorOutput/out/$(PROCESS).out

queue 1
