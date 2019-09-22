import requests


def get_github(id):
    url_repository = "https://api.github.com/users/" + id + "/repos"
    repository_name = []
    number_commit = []
    request_repository = requests.get(url_repository)
    list_repositoy = request_repository.json()
    for i in list_repositoy:
        repository_name.append(i['name'])
    #print(repository_name)

    for name in repository_name:
        url_commit = 'https://api.github.com/repos/' + id + '/' + name + '/commits'
        request_commit = requests.get(url_commit)
        list_commit = request_commit.json()
        number_commit.append(len(list_commit))
    #print(number_commit)
    for s in range(0,len(repository_name)):
        print('Repo: ' + repository_name[s] + ' Number of commits: ' + str(number_commit[s]))


if __name__ == '__main__':
    ID = input('Please input the Github Id\n')
    get_github(ID)
