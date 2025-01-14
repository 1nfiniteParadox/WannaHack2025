## Description
Apache Tomcat's CGI Servlet on an Operating System is vulnerable to RCE when specific conditions are met. Which CGI option's configuration could lead to this vulnerability, and which Operating System is vulnerable?

Flag Format: WannaHack{option-operatingsystem}

## Solution
When running on **Windows with enableCmdLineArguments enabled**, the CGI Servlet is vulnerable to Remote Code Execution due to a bug in the way the JRE passes command line arguments to Windows.

## Flag
WannaHack{enableCmdLineArguments-windows}