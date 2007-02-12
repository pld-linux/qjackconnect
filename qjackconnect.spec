Summary:	Qt based patchbay for Jack Audio Connection Kit
Summary(pl.UTF-8):   Oparty o Qt patchbay dla Jack Audio Connection Kit
Name:		qjackconnect
Version:	0.0.3b
Release:	2
License:	GPL
Group:		X11/Applications/Sound
URL:		http://www.suse.de/~mana/jack.html
Source0:	ftp://ftp.suse.com/pub/people/mana/%{name}-%{version}.tar.bz2
# Source0-md5:	b22c700dcb7b5f856f49b1de526a23d6
Source1:	%{name}.desktop
Patch0:		%{name}-paths_and_flags.patch
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	qt-devel >= 3.1.2
Provides:	jack-patchbay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Qt based patchbay for Jack Audio Connection Kit.

%description -l pl.UTF-8
Oparty o bibliotekę Qt patchbay dla Jack Audio Connection Kit.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f make_qjackconnect \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install -c qjackconnect $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
