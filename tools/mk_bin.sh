proxychains -q git push
git describe | xargs git tag
git describe | xargs proxychains -q git push origin 