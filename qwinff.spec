# defines for the specific github commit
%global gitdate 20171107
%global p1version 0.2.1
%global commit 3420e8ed6c569da4ddd45c72cd261fb6235c4b33
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gver .%{gitdate}git%{shortcommit}
%global vidstr :%{gitdate}git%{shortcommit}

Summary:        An intuitive media converter GUI for ffmpeg
Name:           qwinff
Version:        0.2.2
Release:        0.12%{?gver}%{?dist}
License:        GPLv3
URL:            http://qwinff.github.io/
Source:         https://github.com/qwinff/%{name}/archive/v%{p1version}/%{name}-%{p1version}.tar.gz
Patch1:         https://github.com/qwinff/%{name}/compare/v%{p1version}...%{commit}.patch#/qwinff-post.patch
Patch2:         qwinff-extradefs.patch
Patch3:         https://github.com/qwinff/%{name}/pull/21.patch#/qwinff-perex1.patch
Patch4:         https://github.com/qwinff/%{name}/pull/22.patch#/qwinff-perex2.patch
Patch5:         https://github.com/qwinff/%{name}/pull/23.patch#/qwinff-perex3.patch
Patch6:         https://github.com/qwinff/%{name}/pull/24.patch#/qwinff-perex4.patch
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
#BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  desktop-file-utils
Requires:       ffmpeg
Requires:       sox

%description
QWinFF is a cross-platform, easy-to-use media converter front-end to FFmpeg.
FFmpeg is a powerful command-line utility to convert audio and video file
into numerous formats. QWinFF features a rich set of presets to help users
use FFmpeg easily without having to manually input command-line flags.
Average users can convert multiple media files in just a few clicks,
while advanced users can still adjust conversion parameters in detail.

%prep
%setup -q -n %{name}-%{p1version}
%patch1 -p1 -b .post
%patch2 -p1 -b .extradefs
%patch3 -p1 -b .perex1
%patch4 -p1 -b .perex2
%patch5 -p1 -b .perex3
%patch6 -p1 -b .perex4

%build
%make_build QMAKE=qmake-qt5 %{?_qt5_qmake_flags} \
            LRELEASE=lrelease-qt5 \
            USE_LIBNOTIFY=1 \
            VIDSTR="%{?vidstr}"

%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/qwinff.desktop

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.txt
%doc CHANGELOG.txt README.md
%{_bindir}/qwinff
%{_datadir}/applications/qwinff.desktop
%{_datadir}/pixmaps/qwinff.png
%{_datadir}/qwinff
%{_mandir}/man1/qwinff.1.*

%changelog
* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.2-0.12.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.2-0.11.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.10.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.9.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.8.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.7.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.6.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.5.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.2.2-0.4.20171107git3420e8e
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.2-0.3.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.2-0.2.20171107git3420e8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov  7 2017 Jaroslav Kysela <perex@perex.cz> - 0.2.2-0.1.20171107git3420e8e
- Initial version
