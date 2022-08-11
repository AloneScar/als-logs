const contents = $('#contents');

function getContentNote(note) {
    let content_note =  `
        <div class="content_note" id="n${note.id}">
            <div class="pic">
            <img src="${note.picUrl}" alt="${note.picName}" />
            </div>
            <div class="text">
            <div class="title">
                <h2>${note.title}</h2>
            </div>
            <div class="attribute">
                <span>Type: ${note.type}</span>
                <span>Time: ${note.time}</span>
                <span>Belong: ${note.belong}</span>
                <span>By: ${note.by}</span>
            </div>
            <div class="shortText">${note.shortText}</div>
            <div class="btns">
                <button onclick="javascript: window.location.href='/note/${note.belong}/${note.tittle}'">Read More</button>
            </div>
            </div>
        </div>
    `
    return content_note
}

function getContentDiary(diary) {
    content_diary = `
        <div class="content_diary" id="d${diary.id}">
            <div class="pic">
            <img
                src="${diary.picUrl}"
                alt="${diary.picName}"
            />
            </div>
            <div class="text">
            <div class="title">
                <h2>${diary.title}</h2>
            </div>
            <div class="attribute">
                <span>Type: ${diary.type}</span>
                <span>Belong: ${diary.belong}</span>
                <span>Emotion: ${diary.emotion}</span>
                <span>Weather: ${diary.weather}</span>
                <span>By: ${diary.by}</span>
            </div>
            <div class="shortText">${diary.shortText}</div>
            <div class="btns">
                <button onclick="javascript: window.location.href='/diary/${diary.belong}/${diary.title}'">Read More</button>
            </div>
        </div>
    `
    return content_diary
}

function getContentLink(link) {
    content_link = `
        <div class="content_link" id="l${link.id}">
          <div class="title">
            <img src="${link.imgUrl}" alt="Not Found Pic" />
            <h3>
              <a
                target="_blank"
                href="${link.href}"
                >${link.title}</a
              >
            </h3>
          </div>
          <div class="attribute">
            <span>Type: ${link.type}</span>
            <span>Belong: ${link.belong}</span>
            <span>Time: ${link.time}</span>
          </div>
          <div class="url">
            <a
              target="_blank"
              href="${link.href}"
              >${link.href}</a
            >
            <button
              onclick="copyUrl('${link.href}')"
            >
              Copy
            </button>
          </div>
        </div>
    `
    return content_link
}

function getContentIdea(idea) {
    let content_idea = `
        <div class="content_idea" id="i${idea.id}">
          <div class="time"><h3>${idea.time}</h3></div>
          <div class="text">${idea.textUrl}</div>
        </div>
    `
    return content_idea
}

function copyUrl(url) {
  navigator.clipboard
    .writeText(url)
    .then(swal('Copied Successed', {
      icon: 'success',
      button: false,
      timer: 1000
    }));
}
// lasted running
$(function () {
  $.get("/getHomeContents", (data) => {
    console.log(data);
    data.contents.forEach(content => {
      if (content.type == 'Note') {
        contents.append($(getContentNote(content)))
      } else if (content.type == 'Diary') {
        contents.append($(getContentDiary(content)))
        console.log(getContentDiary(content));
      } else if (content.type == 'Link') {
        contents.append($(getContentLink(content)))
      } else if (content.type == 'Idea') {
        contents.append($(getContentIdea(content)))
      }
    });
  })
})