import math


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages  # 4 photos per page
        self.photos = [[] for page in range(1, pages + 1)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = 0.25 * photos_count
        return cls(math.ceil(pages))

    def add_photo(self, label: str):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {self.photos.index(page) + 1} slot {len(page)}"

        return f"No more free slots"

    def display(self):
        res = []
        for page in self.photos:
            res.append('-----------')
            photos_per_page = ''
            for photo in page:
                photos_per_page += '[] '
            if photos_per_page != '':
                res.append(photos_per_page.strip())
        if res[-1] == '-----------':
            res.append('\n-----------')
        else:
            res.append('-----------')

        return '\n'.join(res)

