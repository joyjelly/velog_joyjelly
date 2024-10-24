import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@noop'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# **Git 사용자 정보 설정**
repo.git.config('user.name', 'github-actions[bot]')
repo.git.config('user.email', 'github-actions[bot]@users.noreply.github.com')

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 변경 사항이 있는지 확인하는 플래그
has_changes = False

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성

        # 깃허브에 파일 추가 (하지만 아직 푸시하지 않음)
        repo.git.add(file_path)
        has_changes = True  # 변경 사항이 발생했음을 표시

# 모든 파일을 커밋한 후 한 번에 커밋과 푸시
if has_changes:
    repo.git.commit('-m', 'Add multiple posts from Velog')
    repo.git.push()
else:
    print("No changes to commit.")
