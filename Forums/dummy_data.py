import models
import stores

post_store = stores.PostStore()
post_store.add(models.Post('Life', 'Life is always great'))
post_store.add(models.Post('Sunshine', 'Sunshine is amazing'))
