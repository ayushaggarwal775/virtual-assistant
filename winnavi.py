import os
from pywinauto.application import Application

def navi(x):
    
    x = ' '.join(x)

    if(x=='open calculator'):
    	Application().start('calc.exe')
    elif(x=='open character map'):
    	os.system(' charmap')
    elif(x=='open disk cleanup utility'):
    	os.system(' cleanmgr')
    elif(x=='open sql client configuration'):
    	os.system(' cliconfg')
    elif(x=='open command prompt'):
    	os.system(' cmd')
    elif(x=='open control panel'):
    	os.system(' control')
    elif(x=='open administrative tools'):
    	os.system('control admintools')
    elif(x=='open display properties'):
    	os.system(' control desktop')
    elif(x=='open folders properties'):
    	os.system(' control folders')
    elif(x=='open fonts'):
    	os.system(' control fonts')
    elif(x=='open keyboard properties'):
    	os.system(' control keyboard')
    elif(x=='open mouse properties'):
    	os.system(' control mouse')
    elif(x=='open network connections'):
    	os.system(' control netconnections')
    elif(x=='open printers and faxes'):
    	os.system(' control printers')
    elif(x=='open scheduled tasks'):
    	os.system(' control schedtasks')
    elif(x=='open opening the windows explorer'):
    	os.system(' explorer')
    elif(x=='open importing or exporting active directory data'):
    	os.system(' csvde')
    elif(x=='open component services'):
    	os.system(' dcomcnfg')
    elif(x=='open dde shares'):
    	os.system(' ddeshare')
    elif(x=='open delete files'):
    	os.system(' del')
    elif(x=='open deleting user profiles'):
    	os.system(' delprof')
    elif(x=='open deleting a folder and all subfolders'):
    	os.system(' deltree')
    elif(x=='open display properties'):
    	os.system(' desk.cpl')
    elif(x=='open device manager'):
    	os.system(' devmgmt.msc')
    elif(x=='open disk defragment'):
    	os.system(' dfrg.msc')
    elif(x=='open phone dialer'):
    	os.system(' dialer')
    elif(x=='open displaying the list of files and folders'):
    	os.system(' dir')
    elif(x=='open disk management'):
    	os.system(' diskmgmt.msc')
    elif(x=='open disk partition manager'):
    	os.system(' diskpart')
    elif(x=='open showing the space used in folders'):
    	os.system(' diskuse')
    elif(x=='open drwatson system troubleshooting utility'):
    	os.system(' drwtsn32')
    elif(x=='open direct x troubleshooter'):
    	os.system(' dxdiag')
    elif(x=='open displaying message on screen'):
    	os.system(' echo')
    elif(x=='open deleting one or more files'):
    	os.system(' erase')
    elif(x=='open event viewer'):
    	os.system(' eventvwr.msc')
    elif(x=='open comparing two files'):
    	os.system(' fc')
    elif(x=='open finding a text string in a file'):
    	os.system(' find')
    elif(x=='open findfast'):
    	os.system(' findfast.cpl')
    elif(x=='open finding for a strings in file'):
    	os.system(' findstr')
    elif(x=='open firefox'):
    	os.system(' firefox')
    elif(x=='open fonts folder'):
    	os.system(' fonts')
    elif(x=='open formatting a disk'):
    	os.system(' format')
    elif(x=='open free cell card game'):
    	os.system(' freecell')
    elif(x=='open checking free disk space'):
    	os.system(' freedisk')
    elif(x=='open shared folders'):
    	os.system(' fsmgmt.msc')
    elif(x=='open bluetooth transfer wizard'):
    	os.system(' fsquirt')
    elif(x=='open know the file and volume utilities'):
    	os.system(' fsutil')
    elif(x=='open file transfer protocl'):
    	os.system(' ftp')
    elif(x=='open knowing file extension'):
    	os.system(' ftype')
    elif(x=='open displaying the mac address'):
    	os.system(' getmac')
    elif(x=='open group policy editor (for xp professional)'):
    	os.system(' gpedit.msc')
    elif(x=='open displaying the resultant set of policy information'):
    	os.system(' gpresult')
    elif(x=='open updating the group policy settings'):
    	os.system(' gpupdate')
    elif(x=='open add hardware wizard'):
    	os.system(' hdwwiz.cpl')
    elif(x=='open online help'):
    	os.system(' help')
    elif(x=='open help and support'):
    	os.system(' helpctr')
    elif(x=='open displaying the host name'):
    	os.system(' hostname')
    elif(x=='open hyperterminal'):
    	os.system(' hypertrm')
    elif(x=='open internet connection wizard'):
    	os.system(' icwconn1')
    elif(x=='open internet explorer'):
    	os.system(' iexplore')
    elif(x=='open iexpress wizard'):
    	os.system(' iexpress')
    elif(x=='open internet properties'):
    	os.system(' inetcpl.cpl')
    elif(x=='open regional settings'):
    	os.system(' intl.cpl')
    elif(x=='open replacing the files that are currently in use by the os'):
    	os.system(' inuse')
    elif(x=='open game controllers'):
    	os.system(' joy.cpl')
    elif(x=='open editing disc label'):
    	os.system(' label')
    elif(x=='open logs you out of windows'):
    	os.system(' logoff')
    elif(x=='open log a user off'):
    	os.system(' logoff')
    elif(x=='open get a log time in a file'):
    	os.system(' logtime')
    elif(x=='open local users and groups'):
    	os.system(' lusrmgr.msc')
    elif(x=='open mouse properties'):
    	os.system(' main.cpl')
    elif(x=='open creating .cab files'):
    	os.system(' makecab')
    elif(x=='open displaying the memory usage'):
    	os.system(' mem')
    elif(x=='open files and settings transfer tool'):
    	os.system(' migwiz')
    elif(x=='open sounds and audio'):
    	os.system(' mmsys.cpl')
    elif(x=='open microsoft syncronization tool'):
    	os.system(' mobsync')
    elif(x=='open microsoft movie maker'):
    	os.system(' moviemk')
    elif(x=='open malicious software removal tool'):
    	os.system(' mrt')
    elif(x=='open system configuration utility'):
    	os.system(' msconfig')
    elif(x=='open hearts card game'):
    	os.system(' mshearts')
    elif(x=='open opening windows installer'):
    	os.system(' msiexec')
    elif(x=='open outlook express'):
    	os.system(' msimn')
    elif(x=='open system information'):
    	os.system(' msinfo32')
    elif(x=='open microsoft paint' or x=='paint'):
    	Application().start('mspaint.exe')
    elif(x=='open remote desktop'):
    	os.system(' mstsc')
    elif(x=='open remote desktop protocol'):
    	os.system(' mstsc')
    elif(x=='open network connections'):
    	os.system(' ncpa.cpl')
    elif(x=='open managing the network resources'):
    	os.system(' net')
    elif(x=='open managing the domain'):
    	os.system(' netdom')
    elif(x=='open network setup wizard'):
    	os.system(' netsetup.cpl')
    elif(x=='open notepad'):
    	Application().start('notepad.exe')
    elif(x=='open removable storage'):
    	os.system(' ntmsmgr.msc')
    elif(x=='open removable storage operator requests'):
    	os.system(' ntmsoprq.msc')
    elif(x=='open user account management'):
    	os.system(' nusrmgr.cpl')
    elif(x=='open odbc data source administrator'):
    	os.system(' odbccp32.cpl')
    elif(x=='open on screen keyboard'):
    	os.system(' osk')
    elif(x=='open object packager'):
    	os.system(' packager')
    elif(x=='open password properties'):
    	os.system(' password.cpl')
    elif(x=='open paint'):
    	os.system(' pbrush')
    elif(x=='open performance monitor'):
    	os.system(' perfmon')
    elif(x=='open performance monitor'):
    	os.system(' perfmon.msc')
    elif(x=='open knowing the permissions for a user'):
    	os.system(' perms')
    elif(x=='open pinball game'):
    	os.system(' pinball')
    elif(x=='open testing a network connecting'):
    	os.system(' ping')
    elif(x=='open power configuration'):
    	os.system(' powercfg.cpl')
    elif(x=='open printing a text file'):
    	os.system(' print')
    elif(x=='open printers folder'):
    	os.system(' printers')
    elif(x=='open shutdown computer'):
    	os.system(' psshutdown')
    elif(x=='open remote access phonebook'):
    	os.system(' rasphone')
    elif(x=='open registry editor'):
    	os.system(' regedit')
    elif(x=='open registry editor'):
    	os.system(' regedit32')
    elif(x=='open resultant set of policy (for xp professional)'):
    	os.system(' rsop.msc')
    elif(x=='open local security settings'):
    	os.system(' secpol.msc')
    elif(x=='open services'):
    	os.system(' services.msc')
    elif(x=='open shuts down windows'):
    	os.system(' shutdown')
    elif(x=='open accessibility controls'):
    	os.system(' access.cpl')
    elif(x=='open accessibility wizard'):
    	os.system(' accwiz')
    elif(x=='open add/remove programs'):
    	os.system(' appwiz.cpl')
    elif(x=='open managing the boot configuration data'):
    	os.system(' bcdedit')
    elif(x=='open editing boot settings'):
    	os.system(' bootcfg')
    elif(x=='open certificate manager'):
    	os.system(' certmgr.msc')
    elif(x=='open check disk utility'):
    	os.system(' chkdsk')
    elif(x=='open indexing service'):
    	os.system(' ciadv.msc')
    elif(x=='open encrypting or decrypting files/folders'):
    	os.system(' cipher')
    elif(x=='open clipboard viewer'):
    	os.system(' clipbrd')
    elif(x=='open clearing the screen'):
    	os.system(' cls')
    elif(x=='open managing stored usernames/passwords'):
    	os.system(' cmdkey')
    elif(x=='open changing cmd color'):
    	os.system(' color')
    elif(x=='open computer management'):
    	os.system(' compmgmt.msc')
    elif(x=='open compressing one or more files'):
    	os.system(' compress')
    elif(x=='open netmeeting'):
    	os.system(' conf')
    elif(x=='open converting fat drives to ntfs'):
    	os.system(' convert')
    elif(x=='open file signature verification tool'):
    	os.system(' sigverif')
    elif(x=='open spider solitare card game'):
    	os.system(' spider')
    elif(x=='open scanners and cameras'):
    	os.system(' sticpl.cpl')
    elif(x=='open system properties'):
    	os.system(' sysdm.cpl')
    elif(x=='open system configuration editor'):
    	os.system(' sysedit')
    elif(x=='open task manager'):
    	os.system(' taskmgr')
    elif(x=='open tcp tester'):
    	os.system(' tcptest')
    elif(x=='open phone and modem options'):
    	os.system(' telephon.cpl')
    elif(x=='open telnet client'):
    	os.system(' telnet')
    elif(x=='open date and time properties'):
    	os.system(' timedate.cpl')
    elif(x=='open utility manager'):
    	os.system(' utilman')
    elif(x=='open driver verifier utility'):
    	os.system(' verifier')
    elif(x=='open windows address book'):
    	os.system(' wab')
    elif(x=='open windows address book import utility'):
    	os.system(' wabmig')
    elif(x=='open microsoft chat'):
    	os.system(' winchat')
    elif(x=='open minesweeper game'):
    	os.system(' winmine')
    elif(x=='open security center'):
    	os.system(' wscui.cpl')
    elif(x=='open automatic updates'):
    	os.system(' wuaucpl.cpl')
    else:
        return False
