Name:       __NAME__
Version:	__VERSION__
Release:	__RELEASE__
Summary:	Yum package manager plugin for private S3 repositories.

Group:      Application/SystemTools
License:    Apache License Version 2.0, January 2004
URL:        https://github.com/seporaitis/yum-s3-iam
Source0:    %{name}-%{version}.tar.gz

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

Requires:	yum
BuildRequires: yum

%description
Yum package manager plugin for private S3 repositories. 
Uses Amazon IAM & EC2 Roles.

%prep
%setup -q

%build
python tests.py 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc s3iam.repo
%doc *E*
/etc/yum/pluginconf.d/*
/usr/lib/yum-plugins/*

%changelog
* Fri May 31 2013 Matt Jamison <matt@mattjamison.com> 1.0-1
Initial packaging
