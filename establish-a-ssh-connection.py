import pexpect 

ip_address = "192.168.56.101"
username = "prne"
password = "cisco123!"
enable_password = "class123!"

try:
    session = pexpect.spawn(f"ssh -o StrictHostKeyChecking=no {username}@{ip_address}", encoding="utf-8", timeout=20)

    session.expect(["password:", pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("enable")
    session.expect(["Password", pexpect.TIMEOUT,pexpect.EOF])
    session.sendline(enable_password)

    session.expect(["#", pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("configure terminal")
    session.expect(["\(config\)#", pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("hostname R1")
    session.expect(["R1\(config\)#", pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("write memory")
    session.expect(["R1\(config\)#", pexpect.TIMEOUT, pexpect.EOF])
    session.sendline("exit")

    print("Configuration successful!")
    session.close()

except Exception as e:
    print("Error:", str(e))
    

