# Maintainer: Michal Krenek (Mikos) <m.krenek@gmail.com>
pkgname=simplespectral
_pkgname=simplespectral
pkgver=1.0.0
pkgrel=1
pkgdesc="Heavily simplified scipy.signal.spectral module which only depends on NumPy and supports pyFFTW"
arch=('any')
url="https://github.com/xmikos/simplespectral"
license=('MIT')
depends=('python' 'python-numpy')
makedepends=('python-setuptools')
source=(https://github.com/xmikos/simplespectral/archive/v$pkgver.tar.gz)

build() {
  cd "$srcdir/${_pkgname}-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-$pkgver"
  python setup.py install --root="$pkgdir"
}

# vim:set ts=2 sw=2 et:
