function genericAJAXRequest(url, method, data) {
	$.ajax({
	  url: url,
	  headers: {
		'Content-Type': 'application/json',
		'Authorization': Cookies.get('sessionid'),
		'X-CSRFToken': Cookies.get('csrftoken'),
	  },
	  method: method,
	  data: JSON.stringify(data),
	  success: (request) => {
		return request;
	  },
	});
};

function rate(post_id, like) {
	const url = (like ? `/ajax/like/${post_id}` : `/ajax/dislike/${post_id}`);
	const data = genericAJAXRequest(url, "get", undefined);
	$(`#total_likes_${post_id}`).text(data.total_likes);
	$(`#total_dislikes_${post_id}`).text(data.total_dislikes);
};

function followUser(user_id) {
	$.ajax({
		url: '/ajax/follow/',
		data: { id: user_id },
		dataType: 'json',
		success: function (data) {
			$(`#follow`).text(data.status);
			$(`#followers`).text(data.count);
			alert('success');
		},
		error: function() {
			alert('error!');
		}
	});
};



function bioChange() {
	event.preventDefault();
	const firstName = $(`#first-name-field`).val();
	const lastName = $(`#last-name-field`).val();
	const bio = $(`#bio-field`).val();
	const location = $(`#location-field`).val();
	$.ajax({
		url: '/ajax/settings/',
		data: { csrfmiddlewaretoken: profileChangeToken, first_name: firstName, last_name: lastName, bio: bio, location: location },
		dataType: 'json',
		type: 'POST',
		success: function (data) {
			$('#first-name-field').val('');
			$('#last-name-field').val('');
			$('#bio-field').val('');
			$('#location-field').val('');
			$('#first_name').text(data.first_name);
			$('#last_name').text(data.last_name);
			$('#bio').text(data.bio);
			$('#location').text(data.location)
			alert('success');
		},
		error: function() {
			alert('error!');
		}
	});
}



function changeProfilePicture() {
	$.ajax({
		url:`/ajax/changepfp`,
		dataType:'json',
		type:'GET',
		success: function (data) {
			alert('success')
		}
	});
}
