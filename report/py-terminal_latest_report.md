# Container Vulnerability Report
**Image:** `py-terminal:latest`

## Target: py-terminal:latest (debian 13.6)
| ID | Package | Severity | Status | Installed | Fixed | Title |
|---|---|---|---|---|---|---|
| CVE-2011-3374 | apt | LOW | affected | 3.0.3 |  | It was found that apt-key in apt, all versions, do not correctly valid ... |
| TEMP-0841856-B18BAF | bash | LOW | affected | 5.2.37-2+b9 |  | [Privilege escalation possible to other user than root] |
| CVE-2026-53615 | bsdutils | HIGH | affected | 1:2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | bsdutils | MEDIUM | affected | 1:2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | bsdutils | MEDIUM | affected | 1:2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | bsdutils | MEDIUM | affected | 1:2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | bsdutils | LOW | affected | 1:2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | bsdutils | LOW | affected | 1:2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | bsdutils | UNKNOWN | affected | 1:2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | bsdutils | UNKNOWN | affected | 1:2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | bsdutils | UNKNOWN | affected | 1:2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2017-18018 | coreutils | LOW | affected | 9.7-3 |  | coreutils: race condition vulnerability in chown and chgrp |
| CVE-2025-5278 | coreutils | LOW | affected | 9.7-3 |  | coreutils: Heap Buffer Under-Read in GNU Coreutils sort via Key Specification |
| CVE-2026-56391 | coreutils | LOW | affected | 9.7-3 |  | coreutils: GNU coreutils uniq: Denial of Service and information disclosure via out-of-bounds read with multibyte input |
| CVE-2026-56392 | coreutils | LOW | affected | 9.7-3 |  | coreutils: GNU coreutils unexpand: Denial of Service via crafted tab stop values |
| CVE-2026-53910 | diffutils | LOW | affected | 1:3.10-4 |  | diff3tool from GNU diffutilsis vulnerable to a heap\u2011based buffer  ... |
| CVE-2026-41992 | gzip | HIGH | affected | 1.13-1 |  | GNU gzip contains a global buffer overflow vulnerability in the LZH de ... |
| CVE-2026-41991 | gzip | MEDIUM | affected | 1.13-1 |  | gzip: gzip: Arbitrary file overwrite via insecure temporary file handling in gzexe utility |
| CVE-2026-54369 | libacl1 | HIGH | affected | 2.3.2-2+b1 |  | acl: Symlink traversal privilege escalation via libacl functions |
| CVE-2026-54370 | libacl1 | MEDIUM | affected | 2.3.2-2+b1 |  | acl: TOCTOU Symlink Traversal via getfacl/setfacl |
| CVE-2011-3374 | libapt-pkg7.0 | LOW | affected | 3.0.3 |  | It was found that apt-key in apt, all versions, do not correctly valid ... |
| CVE-2026-54371 | libattr1 | MEDIUM | affected | 1:2.5.2-3 |  | attr: Symlink Traversal Privilege Escalation via getfattr and setfattr |
| CVE-2026-53615 | libblkid1 | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | libblkid1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | libblkid1 | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | libblkid1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | libblkid1 | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | libblkid1 | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | libblkid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | libblkid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | libblkid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2026-42250 | libbz2-1.0 | MEDIUM | affected | 1.0.8-6 |  | bzip2: bzip2: Denial of Service in bzip2recover via a specially crafted file |
| CVE-2026-5435 | libc-bin | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Out-of-bounds write via TSIG record processing |
| CVE-2026-5450 | libc-bin | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Heap Buffer Overflow in `scanf` with `%mc` format specifier and large width |
| CVE-2026-5928 | libc-bin | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Information disclosure or denial of service via ungetwc function with specific wide character encodings |
| CVE-2026-6238 | libc-bin | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Application crash or uninitialized memory read via crafted DNS response |
| CVE-2010-4756 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: glob implementation can cause excessive CPU and memory consumption due to crafted glob expressions |
| CVE-2018-20796 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c |
| CVE-2019-1010022 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: stack guard protection bypass |
| CVE-2019-1010023 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: running ldd on malicious ELF leads to code execution because of wrong size computation |
| CVE-2019-1010024 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: ASLR bypass using cache of thread stack and heap |
| CVE-2019-1010025 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: information disclosure of heap addresses of pthread_created thread |
| CVE-2019-9192 | libc-bin | LOW | affected | 2.41-12+deb13u3 |  | glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c |
| CVE-2026-5435 | libc6 | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Out-of-bounds write via TSIG record processing |
| CVE-2026-5450 | libc6 | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Heap Buffer Overflow in `scanf` with `%mc` format specifier and large width |
| CVE-2026-5928 | libc6 | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Information disclosure or denial of service via ungetwc function with specific wide character encodings |
| CVE-2026-6238 | libc6 | MEDIUM | affected | 2.41-12+deb13u3 |  | glibc: glibc: Application crash or uninitialized memory read via crafted DNS response |
| CVE-2010-4756 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: glob implementation can cause excessive CPU and memory consumption due to crafted glob expressions |
| CVE-2018-20796 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c |
| CVE-2019-1010022 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: stack guard protection bypass |
| CVE-2019-1010023 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: running ldd on malicious ELF leads to code execution because of wrong size computation |
| CVE-2019-1010024 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: ASLR bypass using cache of thread stack and heap |
| CVE-2019-1010025 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: information disclosure of heap addresses of pthread_created thread |
| CVE-2019-9192 | libc6 | LOW | affected | 2.41-12+deb13u3 |  | glibc: uncontrolled recursion in function check_dst_limits_calc_pos_1 in posix/regexec.c |
| CVE-2026-53615 | liblastlog2-2 | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | liblastlog2-2 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | liblastlog2-2 | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | liblastlog2-2 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | liblastlog2-2 | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | liblastlog2-2 | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | liblastlog2-2 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | liblastlog2-2 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | liblastlog2-2 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2026-53615 | libmount1 | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | libmount1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | libmount1 | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | libmount1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | libmount1 | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | libmount1 | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | libmount1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | libmount1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | libmount1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2025-69720 | libncursesw6 | HIGH | affected | 6.5+20250216-2 |  | ncurses: ncurses: Buffer overflow vulnerability may lead to arbitrary code execution. |
| CVE-2025-6141 | libncursesw6 | LOW | affected | 6.5+20250216-2 |  | gnu-ncurses: ncurses Stack Buffer Overflow |
| CVE-2026-54411 | libpam-modules | MEDIUM | fix_deferred | 1.7.0-5 |  | linux-pam: Plaintext password recovery via timing discrepancy in pam_userdb module |
| CVE-2026-54411 | libpam-modules-bin | MEDIUM | fix_deferred | 1.7.0-5 |  | linux-pam: Plaintext password recovery via timing discrepancy in pam_userdb module |
| CVE-2026-54411 | libpam-runtime | MEDIUM | fix_deferred | 1.7.0-5 |  | linux-pam: Plaintext password recovery via timing discrepancy in pam_userdb module |
| CVE-2026-54411 | libpam0g | MEDIUM | fix_deferred | 1.7.0-5 |  | linux-pam: Plaintext password recovery via timing discrepancy in pam_userdb module |
| CVE-2026-53615 | libsmartcols1 | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | libsmartcols1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | libsmartcols1 | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | libsmartcols1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | libsmartcols1 | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | libsmartcols1 | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | libsmartcols1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | libsmartcols1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | libsmartcols1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2026-11822 | libsqlite3-0 | MEDIUM | affected | 3.46.1-7+deb13u1 |  | SQLite before 3.53.2 contains memory corruption vulnerabilities in the ... |
| CVE-2026-11824 | libsqlite3-0 | MEDIUM | affected | 3.46.1-7+deb13u1 |  | SQLite before 3.53.2 contains a heap-based buffer overflow vulnerabili ... |
| CVE-2026-50812 | libsqlite3-0 | MEDIUM | affected | 3.46.1-7+deb13u1 |  | A NULL pointer dereference in the SQLite Session Extension in SQLite 3 ... |
| CVE-2026-50813 | libsqlite3-0 | MEDIUM | affected | 3.46.1-7+deb13u1 |  | An issue in SQLite before Fossil check-in 869a51ae84df allows a local  ... |
| CVE-2021-45346 | libsqlite3-0 | LOW | affected | 3.46.1-7+deb13u1 |  | sqlite: crafted SQL query allows a malicious user to obtain sensitive information |
| CVE-2025-70873 | libsqlite3-0 | LOW | affected | 3.46.1-7+deb13u1 |  | sqlite: SQLite: Information Disclosure via Crafted ZIP File |
| CVE-2013-4392 | libsystemd0 | LOW | affected | 257.13-1~deb13u1 |  | systemd: TOCTOU race condition when updating file permissions and SELinux security contexts |
| CVE-2023-31437 | libsystemd0 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can modify a seale ... |
| CVE-2023-31438 | libsystemd0 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can truncate a sea ... |
| CVE-2023-31439 | libsystemd0 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can modify the con ... |
| CVE-2026-40228 | libsystemd0 | LOW | affected | 257.13-1~deb13u1 |  | systemd: systemd-journald: Unintended output to user terminals via logger command |
| CVE-2025-69720 | libtinfo6 | HIGH | affected | 6.5+20250216-2 |  | ncurses: ncurses: Buffer overflow vulnerability may lead to arbitrary code execution. |
| CVE-2025-6141 | libtinfo6 | LOW | affected | 6.5+20250216-2 |  | gnu-ncurses: ncurses Stack Buffer Overflow |
| CVE-2013-4392 | libudev1 | LOW | affected | 257.13-1~deb13u1 |  | systemd: TOCTOU race condition when updating file permissions and SELinux security contexts |
| CVE-2023-31437 | libudev1 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can modify a seale ... |
| CVE-2023-31438 | libudev1 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can truncate a sea ... |
| CVE-2023-31439 | libudev1 | LOW | affected | 257.13-1~deb13u1 |  | An issue was discovered in systemd 253. An attacker can modify the con ... |
| CVE-2026-40228 | libudev1 | LOW | affected | 257.13-1~deb13u1 |  | systemd: systemd-journald: Unintended output to user terminals via logger command |
| CVE-2026-53615 | libuuid1 | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | libuuid1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | libuuid1 | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | libuuid1 | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | libuuid1 | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | libuuid1 | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | libuuid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | libuuid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | libuuid1 | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2026-53615 | login | HIGH | affected | 1:4.16.0-2+really2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | login | MEDIUM | affected | 1:4.16.0-2+really2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | login | MEDIUM | affected | 1:4.16.0-2+really2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | login | MEDIUM | affected | 1:4.16.0-2+really2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | login | LOW | affected | 1:4.16.0-2+really2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | login | LOW | affected | 1:4.16.0-2+really2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | login | UNKNOWN | affected | 1:4.16.0-2+really2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | login | UNKNOWN | affected | 1:4.16.0-2+really2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | login | UNKNOWN | affected | 1:4.16.0-2+really2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2007-5686 | login.defs | LOW | affected | 1:4.17.4-2 |  | initscripts in rPath Linux 1 sets insecure permissions for the /var/lo ... |
| CVE-2024-56433 | login.defs | LOW | affected | 1:4.17.4-2 |  | shadow-utils: Default subordinate ID configuration in /etc/login.defs could lead to compromise |
| TEMP-0628843-DBAD28 | login.defs | LOW | affected | 1:4.17.4-2 |  | [more related to CVE-2005-4890] |
| CVE-2026-53615 | mount | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | mount | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | mount | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | mount | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | mount | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | mount | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | mount | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | mount | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | mount | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2025-69720 | ncurses-base | HIGH | affected | 6.5+20250216-2 |  | ncurses: ncurses: Buffer overflow vulnerability may lead to arbitrary code execution. |
| CVE-2025-6141 | ncurses-base | LOW | affected | 6.5+20250216-2 |  | gnu-ncurses: ncurses Stack Buffer Overflow |
| CVE-2025-69720 | ncurses-bin | HIGH | affected | 6.5+20250216-2 |  | ncurses: ncurses: Buffer overflow vulnerability may lead to arbitrary code execution. |
| CVE-2025-6141 | ncurses-bin | LOW | affected | 6.5+20250216-2 |  | gnu-ncurses: ncurses Stack Buffer Overflow |
| CVE-2007-5686 | passwd | LOW | affected | 1:4.17.4-2 |  | initscripts in rPath Linux 1 sets insecure permissions for the /var/lo ... |
| CVE-2024-56433 | passwd | LOW | affected | 1:4.17.4-2 |  | shadow-utils: Default subordinate ID configuration in /etc/login.defs could lead to compromise |
| TEMP-0628843-DBAD28 | passwd | LOW | affected | 1:4.17.4-2 |  | [more related to CVE-2005-4890] |
| CVE-2026-13221 | perl-base | CRITICAL | affected | 5.40.1-6 |  | Perl versions through 5.43.9 produce silently incorrect regular expres ... |
| CVE-2026-42496 | perl-base | CRITICAL | fix_deferred | 5.40.1-6 |  | perl-archive-tar: perl-archive-tar: Path traversal via crafted symlinks allows arbitrary file access |
| CVE-2026-57433 | perl-base | CRITICAL | affected | 5.40.1-6 |  | Storable versions before 3.41 for Perl have a signed integer overflow  ... |
| CVE-2026-8376 | perl-base | CRITICAL | affected | 5.40.1-6 |  | perl: Perl: Heap buffer overflow when compiling regular expressions on 32-bit builds |
| CVE-2026-42497 | perl-base | HIGH | fix_deferred | 5.40.1-6 |  | perl-Archive-Tar: perl-Archive-Tar: Arbitrary file modification via crafted hardlinks during archive extraction |
| CVE-2026-48962 | perl-base | HIGH | affected | 5.40.1-6 |  | perl-IO-Compress: perl-IO-Compress: Arbitrary code execution via attacker-controlled output glob |
| CVE-2026-57432 | perl-base | HIGH | affected | 5.40.1-6 |  | Perl versions through 5.43.10 have an integer overflow in S_measure_st ... |
| CVE-2026-9538 | perl-base | HIGH | fix_deferred | 5.40.1-6 |  | perl-Archive-Tar: perl-Archive-Tar: Denial of Service via crafted tar header with large entry size |
| CVE-2025-15649 | perl-base | MEDIUM | affected | 5.40.1-6 |  | perl-IO-Compress: perl-IO-Compress: Denial of Service via malformed DOS date in zip header |
| CVE-2026-12087 | perl-base | MEDIUM | affected | 5.40.1-6 |  | perl-Socket: perl-Socket: Information Disclosure due to Out-of-Bounds Read |
| CVE-2026-48959 | perl-base | MEDIUM | affected | 5.40.1-6 |  | perl-IO-Compress: perl-IO-Compress: CPU exhaustion via per-byte read loop in fastForward |
| CVE-2026-48961 | perl-base | MEDIUM | affected | 5.40.1-6 |  | perl-IO-Compress: IO::Compress: Denial of Service in zipdetails CLI tool via malformed Info-ZIP Unix Extra Field |
| CVE-2026-7010 | perl-base | MEDIUM | affected | 5.40.1-6 |  | HTTP::Tiny versions before 0.093 for Perl do not validate CRLF in HTTP ... |
| CVE-2011-4116 | perl-base | LOW | affected | 5.40.1-6 |  | perl: File:: Temp insecure temporary file handling |
| CVE-2026-7017 | perl-base | UNKNOWN | affected | 5.40.1-6 |  | HTTP::Tiny versions before 0.095 for Perl forward credential headers t ... |
| TEMP-0517018-A83CE6 | sysvinit-utils | LOW | affected | 3.14-4 |  | [sysvinit: no-root option in expert installer exposes locally exploitable security flaw] |
| CVE-2026-5704 | tar | MEDIUM | affected | 1.35+dfsg-3.1 |  | tar: tar: Hidden file injection via crafted archives |
| CVE-2005-2541 | tar | LOW | affected | 1.35+dfsg-3.1 |  | tar: does not properly warn the user when extracting setuid or setgid files |
| TEMP-0290435-0B57B5 | tar | LOW | affected | 1.35+dfsg-3.1 |  | [tar's rmt command may have undesired side effects] |
| CVE-2026-53615 | util-linux | HIGH | affected | 2.41-5 |  | [Integer Overflow or Wraparound in libblkid/src/partitions/dos.c] |
| CVE-2026-13595 | util-linux | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: heap use-after-free in libblkid nested partition probing |
| CVE-2026-27456 | util-linux | MEDIUM | affected | 2.41-5 |  | util-linux: TOCTOU in the mount program when setting up loop devices |
| CVE-2026-3184 | util-linux | MEDIUM | affected | 2.41-5 |  | util-linux: util-linux: Access control bypass due to improper hostname canonicalization |
| CVE-2022-0563 | util-linux | LOW | affected | 2.41-5 |  | util-linux: partial disclosure of arbitrary files in chfn and chsh when compiled with libreadline |
| CVE-2025-14104 | util-linux | LOW | affected | 2.41-5 |  | util-linux: util-linux: Heap buffer overread in setpwnam() when processing 256-byte usernames |
| CVE-2026-53612 | util-linux | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) hook_owner.c chmod/chown] |
| CVE-2026-53613 | util-linux | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via TOCTOU in mount(8) - Target Path Redirection] |
| CVE-2026-53614 | util-linux | UNKNOWN | affected | 2.41-5 |  | [Local Privilege Escalation via LIBMOUNT_FORCE_MOUNT2 Environment Variable - nosuid/noexec Bypass in SUID mount(8)] |
| CVE-2026-27171 | zlib1g | MEDIUM | affected | 1:1.3.dfsg+really1.3.1-1+b1 |  | zlib: zlib: Denial of Service via infinite loop in CRC32 combine functions |

## Target: Python
| ID | Package | Severity | Status | Installed | Fixed | Title |
|---|---|---|---|---|---|---|
| CVE-2025-8869 | pip | MEDIUM | fixed | 25.0.1 | 25.3 | pip: pip missing checks on symbolic link extraction |
| CVE-2026-3219 | pip | MEDIUM | fixed | 25.0.1 | 26.1 | pip: pip: Incorrect file installation due to improper archive handling |
| CVE-2026-6357 | pip | MEDIUM | fixed | 25.0.1 | 26.1 | pip: pip: Arbitrary code execution or information disclosure via malicious wheel package installation |
| CVE-2026-8643 | pip | MEDIUM | fixed | 25.0.1 | 26.1.2 | python-pip: Path traversal via malicious entry point name in pip wheel installation allows arbitrary file overwrite |
| CVE-2026-1703 | pip | LOW | fixed | 25.0.1 | 26.0 | pip: pip: Information disclosure via path traversal when installing crafted wheel archives |
