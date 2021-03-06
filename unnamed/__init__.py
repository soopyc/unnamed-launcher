#  Copyright (c) 2021 kcomain and contributors
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
from git import InvalidGitRepositoryError
from git.repo import Repo


class SemVer:
    __slots__ = ("major", "minor", "patch", "release", "rev")

    def __init__(self, major, minor, patch, release=None):
        self.major = major
        self.minor = minor
        self.patch = patch
        try:
            self.rev = Repo().rev_parse("HEAD")
        except InvalidGitRepositoryError:
            self.rev = None
        except Exception:
            print("[!] unable to get git reference due to unknown error. it is safe to ignore this message")
            self.rev = None
        self.release = release.lower()

    @property
    def revision(self):
        return str(self.rev)[:7] if self.rev else ""

    @property
    def numerical_string(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __str__(self):
        return f"{self.numerical_string}-{self.release}"


VERSION = SemVer(0, 1, 1, "alpha")
