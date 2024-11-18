class solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used_names = set()
        result = []
        for name in names:
            if name not in used_names:
                result.append(name)
                used_names.add(name)
            else:
                suffix = 1
                while f"{name}_{suffix}" in used_names:
                    suffix += 1
                result.append(f"{name}_{suffix}")
                used_names.add(f"{name}_{suffix}")
        return result