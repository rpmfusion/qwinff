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
Release:        0.1%{?gver}%{?dist}
License:        GPLv3
URL:            http://qwinff.github.io/
Source:         https://github.com/qwinff/%{name}/archive/v%{p1version}/%{name}-%{p1version}.tar.gz
Patch1:         https://github.com/qwinff/%{name}/compare/v%{p1version}...%{commit}.patch#/qwinff-post.patch
Patch2:         qwinff-extradefs.patch
Patch3:         https://github.com/qwinff/%{name}/pull/21.patch#/qwinff-perex1.patch
Patch4:         https://github.com/qwinff/%{name}/pull/22.patch#/qwinff-perex2.patch
Patch5:         https://github.com/qwinff/%{name}/pull/23.patch#/qwinff-perex3.patch
Patch6:         https://github.com/qwinff/%{name}/pull/24.patch#/qwinff-perex4.patch
BuildRequires:  qt5-devel
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
* Tue Nov  7 2017 Jaroslav Kysela <perex@perex.cz> - 0.2.2-0.1.20171107git3420e8e
- Initial version