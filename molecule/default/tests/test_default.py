def test_hosts_file(host):
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.is_file
