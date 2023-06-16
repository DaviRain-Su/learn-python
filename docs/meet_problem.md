#  error: subprocess-exited-with-error

```
 × Getting requirements to build wheel did not run successfully.
 │ exit code: 1
 ╰─> [76 lines of output]
     <string>:63: RuntimeWarning: NumPy 1.21.0 may not yet support Python 3.10.
     Running from numpy source directory.
     running egg_info
     running build_src
     build_src
     creating numpy.egg-info
     writing numpy.egg-info/PKG-INFO
```
这个问题怎么解决呢？

这个问题出现的原因是由于使用的 `NumPy` 版本可能不完全兼容 Python 3.10。为了解决这个问题，你可以尝试以下几个步骤：

1. 更新 `NumPy` 版本：检查你的 `requirements.txt` 文件中 `NumPy` 的版本号是否过低。如果是的话，可以尝试升级到最新的 `NumPy` 版本，看是否能解决兼容性问题。可以在 `requirements.txt` 文件中将 `numpy` 的行改为类似以下形式：

```
numpy>=1.21.2
```

这将会要求安装大于或等于 1.21.2 版本的 `NumPy`。

2. 确认 `NumPy` 支持 Python 3.10：访问 `NumPy` 的官方网站或查阅它们的文档，确认你所使用的 `NumPy` 版本是否支持 Python 3.10。有时候需要等待 `NumPy` 更新以支持最新的 Python 版本。如果官方版本尚不支持 Python 3.10，你可以尝试等待或选择一个与 Python 3.10 兼容的较新版本。

3. 检查其他依赖项：除了 `NumPy`，还有其他依赖项可能与 Python 3.10 不兼容。确保你的 `requirements.txt` 文件中的所有依赖项都与 Python 3.10 兼容。可以尝试更新其他库的版本，以确保与 Python 3.10 兼容。

4. 检查 Python 版本和环境：确认你正在使用的 Python 版本是 3.10，并且你的开发环境和虚拟环境也与 Python 3.10 兼容。有时候使用不同的 Python 版本可能导致一些兼容性问题。

如果上述步骤无法解决问题，你可能需要等待 `NumPy` 更新或寻求 `NumPy` 社区的支持。同时，你也可以尝试在开发环境中使用其他较早版本的 Python，或者选择一个与 `NumPy` 兼容的较新版本。
