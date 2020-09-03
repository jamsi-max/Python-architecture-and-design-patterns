from controllers import Index, About, Contacts

routes = {
    '/': Index(),
    'about/': About(),
    'contacts/': Contacts(),
}
