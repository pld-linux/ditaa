# TODO:
# - doesn't build (some varargs problem with jdk 1.6)
# - use system jars (see lib subdir)
%include	/usr/lib/rpm/macros.java
Summary:	DIagrams Through Ascii Art
Summary(pl.UTF-8):	DIagrams Through Ascii Art - tworzenie diagramów za pomocą ASCII art
Name:		ditaa
Version:	0.9
Release:	0.1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ditaa/ditaa0_9-src.zip
# Source0-md5:	d7230273bf4c28c5029d350842278cf9
URL:		http://ditaa.sourceforge.net/
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art ('drawings' that contain
characters that resemble lines like | / -), into proper bitmap
graphics.

%description -l pl.UTF-8
ditaa to małe narzędzie działające z linii poleceń, napisane w Javie,
potrafiące konwertować diagramy rysowane przy użyciu ASCII art
("rysunków" zawierających znaki przypominające linie, takie jak | / -)
we właściwą grafikę bitmapową.

%prep
%setup -q -c

sed -i -e 's/source="1\.6"/source="1.5"/' build/release.xml

%build
export JAVA_HOME="%{java_home}"

#required_jars="..."
#CLASSPATH=$(build-classpath $required_jars)
#export CLASSPATH

%ant -f build/release.xml release-jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}

cp -a releases/ditaa0_9.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf ditaa0_9.jar $RPM_BUILD_ROOT%{_javadir}/ditaa.jar

cat >$RPM_BUILD_ROOT%{_bindir}/ditaa <<EOF
#!/bin/sh

java -jar %{_javadir}/ditaa.jar "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY
%attr(755,root,root) %{_bindir}/ditaa
%{_javadir}/ditaa0_9.jar
%{_javadir}/ditaa.jar
