

function showSection(section) {

    document.getElementById("dashboard-section").classList.add("d-none");
    document.getElementById("vendors-section").classList.add("d-none");
    document.getElementById("events-section").classList.add("d-none");
    document.getElementById("users-section").classList.add("d-none");
    document.getElementById("user-detail-section").classList.add("d-none");

    document.getElementById(section + "-section")
        .classList.remove("d-none");
}



async function loadDashboardSummary() {
    try {
        const response = await fetch("/dashboard/summary/");

        if (!response.ok) {
            throw new Error("Failed to load dashboard summary.");
        }

        const data = await response.json();

        document.getElementById("customer-count").textContent = data.customers;
        document.getElementById("vendor-count").textContent = data.vendors;
        document.getElementById("event-count").textContent = data.events;
        document.getElementById("booking-count").textContent = data.bookings;

    } catch (error) {
        console.error("Dashboard summary error:", error);
    }
}

loadDashboardSummary();



async function loadVendors() {
    try {
        const response = await fetch("/api/vendors/");

        if (!response.ok) {
            throw new Error("Failed to load vendors.");
        }

        const data = await response.json();

        const vendors = data.results || data;

        const container = document.getElementById("vendors-list");

        container.innerHTML = "";

        vendors.forEach(vendor => {
            container.innerHTML += `
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="card-body">

                            <h5 class="card-title mb-3">
                                ${vendor.name}
                            </h5>

                            <p class="mb-2">
                                <strong>Email:</strong>
                                ${vendor.email}
                            </p>

                            <p class="mb-2">
                                <strong>Phone:</strong>
                                ${vendor.phone}
                            </p>

                            <p class="text-muted mb-0">
                                ${vendor.address}
                            </p>

                        </div>

                        <div class="card-footer bg-white border-0">
                           
                            <button
                                class="btn btn-sm btn-outline-primary"
                                onclick="openEditVendorModal(${vendor.id})"
                            >
                                Edit
                            </button>
                        </div>
                    </div>
                </div>
            `;
        });

    } catch (error) {
        console.error("Vendor loading error:", error);
    }
}

loadVendors();





let editingVendorId = null;


function openAddVendorModal() {

    editingVendorId = null;

    document.getElementById("vendorModalTitle").textContent = "Add Vendor";

    document.getElementById("vendor-name").value = "";
    document.getElementById("vendor-email").value = "";
    document.getElementById("vendor-phone").value = "";
    document.getElementById("vendor-address").value = "";
}


async function openEditVendorModal(vendorId) {

    try {
        const response = await fetch(`/api/vendors/${vendorId}/`);

        if (!response.ok) {
            console.log("Status:", response.status);
            console.log("Response:", await response.text());
            throw new Error("Failed to load vendor.");
        }

        const vendor = await response.json();

        editingVendorId = vendor.id;

        document.getElementById("vendorModalTitle").textContent = "Edit Vendor";

        document.getElementById("vendor-name").value = vendor.name;
        document.getElementById("vendor-email").value = vendor.email;
        document.getElementById("vendor-phone").value = vendor.phone;
        document.getElementById("vendor-address").value = vendor.address;

        const modal = new bootstrap.Modal(
            document.getElementById("vendorModal")
        );

        modal.show();

    } catch (error) {
        console.error("Vendor edit error:", error);
    }
}

async function saveVendor() {

    const vendorData = {
        name: document.getElementById("vendor-name").value,
        email: document.getElementById("vendor-email").value,
        phone: document.getElementById("vendor-phone").value,
        address: document.getElementById("vendor-address").value
    };

    let url = "/api/vendors/";
    let method = "POST";

    if (editingVendorId) {
        url = `/api/vendors/${editingVendorId}/`;
        method = "PUT";
    }

    try {

        const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: JSON.stringify(vendorData)
        });

        const data = await response.json();

        if (!response.ok) {
            console.error(data);
            alert("Failed to save vendor.");
            return;
        }

        bootstrap.Modal
            .getInstance(document.getElementById("vendorModal"))
            .hide();

        await loadVendors();

    } catch (error) {
        console.error("Vendor save error:", error);
    }
}








function formatEventDate(dateString) {
    const date = new Date(dateString);

    return date.toLocaleString("en-IN", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        hour12: true
    });
}

async function loadEvents() {
    console.log("Apply clicked");
    try {
        const search = document.getElementById("event-search").value;
        const dateFrom = document.getElementById("event-date-from").value;
        const dateTo = document.getElementById("event-date-to").value;

        const params = new URLSearchParams();

        if (search) {
            params.append("search", search);
        }

        if (dateFrom) {
            params.append("event_date__gte", `${dateFrom}T00:00:00`);
        }

        if (dateTo) {
            params.append("event_date__lte", `${dateTo}T23:59:59`);
        }

        const response = await fetch(
            `/api/events/?${params.toString()}`
        );

        if (!response.ok) {
            throw new Error("Failed to load events.");
        }

        const data = await response.json();

        const events = data.results || data;

        const container = document.getElementById("events-list");

        container.innerHTML = "";

        events.forEach(event => {
            container.innerHTML += `
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="card-body">

                            <h5 class="card-title mb-3">
                                ${event.name}
                            </h5>

                            <p class="mb-2">
                                <strong>Vendor:</strong>
                                ${event.vendor_name}
                            </p>

                            <p class="mb-2">
                                <strong>Date:</strong>
                                ${formatEventDate(event.event_date)}
                            </p>

                            <p class="mb-2">
                                <strong>Total Seats:</strong>
                                ${event.total_seats}
                            </p>

                            <p class="text-muted mb-0">
                                ${event.description}
                            </p>

                        </div>

                        <div class="card-footer bg-white border-0">
                            <button
                                class="btn btn-sm btn-outline-primary"
                                onclick="openEditEventModal(${event.id})"
                            >
                                Edit
                            </button>
                        </div>
                    </div>
                </div>
            `;
        });

    } catch (error) {
        console.error("Event loading error:", error);
    }
}

loadEvents();



async function loadEventVendors() {
    try {
        const response = await fetch("/api/vendors/");

        if (!response.ok) {
            throw new Error("Failed to load vendors.");
        }

        const data = await response.json();
        const vendors = data.results || data;

        const select = document.getElementById("event-vendor");

        select.innerHTML = `
            <option value="">Select Vendor</option>
        `;

        vendors.forEach(vendor => {
            select.innerHTML += `
                <option value="${vendor.id}">
                    ${vendor.name}
                </option>
            `;
        });

    } catch (error) {
        console.error("Event vendor loading error:", error);
    }
}
loadEventVendors();



function openAddEventModal() {

    editingEventId = null;

    document.getElementById("eventModalTitle").textContent = "Add Event";

    document.getElementById("event-name").value = "";
    document.getElementById("event-vendor").value = "";
    document.getElementById("event-description").value = "";
    document.getElementById("event-date").value = "";
    document.getElementById("event-total-seats").value = "";

    loadEventVendors();
}


async function saveEvent() {

    const eventData = {
        name: document.getElementById("event-name").value,
        vendor: document.getElementById("event-vendor").value,
        description: document.getElementById("event-description").value,
        event_date: document.getElementById("event-date").value,
        total_seats: document.getElementById("event-total-seats").value
    };

    try {
        let url = "/api/events/";
        let method = "POST";

        if (editingEventId) {
            url = `/api/events/${editingEventId}/`;
            method = "PUT";
        }

        const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: JSON.stringify(eventData)
        });

        const data = await response.json();

        if (!response.ok) {
            console.error("Event save error:", data);
            alert("Failed to save event.");
            return;
        }

        bootstrap.Modal
            .getInstance(document.getElementById("eventModal"))
            .hide();

        await loadEvents();

    } catch (error) {
        console.error("Event save error:", error);
    }
}


let editingEventId = null;

async function openEditEventModal(eventId) {
    try {
        const response = await fetch(`/api/events/${eventId}/`);

        if (!response.ok) {
            console.log("Status:", response.status);
            console.log("Response:", await response.text());
            throw new Error("Failed to load event.");
        }

        const event = await response.json();

        editingEventId = event.id;

        document.getElementById("eventModalTitle").textContent = "Edit Event";

        document.getElementById("event-name").value = event.name;
        document.getElementById("event-description").value = event.description;
        document.getElementById("event-date").value = event.event_date.slice(0, 16);
        document.getElementById("event-total-seats").value = event.total_seats;

        await loadEventVendors();

        document.getElementById("event-vendor").value = event.vendor;

        const modal = new bootstrap.Modal(
            document.getElementById("eventModal")
        );

        modal.show();

    } catch (error) {
        console.error("Event edit error:", error);
    }
}


let usersNextUrl = null;
let usersPreviousUrl = null;

async function loadUsers(url = "/api/auth/user/") {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Failed to load users.");
        }

        const data = await response.json();

        const users = data.results || data;

        usersNextUrl = data.next || null;
        usersPreviousUrl = data.previous || null;

        const container = document.getElementById("users-list");

        container.innerHTML = "";

        users.forEach(user => {
            container.innerHTML += `
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="card-body">

                            <h5 class="card-title mb-3">
                                ${user.username}
                            </h5>

                            <p class="mb-2">
                                <strong>Email:</strong>
                                ${user.email}
                            </p>

                            <p class="mb-2">
                                <strong>Name:</strong>
                                ${user.first_name} ${user.last_name}
                            </p>

                            <p class="text-muted mb-0">
                                <strong>Referral Code:</strong>
                                ${user.referral_code}
                            </p>

                        </div>

                        <div class="card-footer bg-white border-0">
                            <button
                                class="btn btn-sm btn-outline-primary"
                                onclick="openUserDetails(${user.id})"
                            >
                                View Details
                            </button>
                        </div>
                    </div>
                </div>
            `;
        });

        document.getElementById("users-previous").disabled =
            !usersPreviousUrl;

        document.getElementById("users-next").disabled =
            !usersNextUrl;

    } catch (error) {
        console.error("User loading error:", error);
    }
}

loadUsers();




async function openUserDetails(userId) {
    try {
        const userResponse = await fetch(`/api/auth/user/${userId}/`);

        if (!userResponse.ok) {
            throw new Error("Failed to load user details.");
        }

        const user = await userResponse.json();

        const treeResponse = await fetch(`/api/referrals/${userId}/tree/`);

        if (!treeResponse.ok) {
            throw new Error("Failed to load referral tree.");
        }

        const treeData = await treeResponse.json();
        const tree = treeData.tree || treeData;

        showSection("user-detail");

        document.getElementById("user-detail-username").textContent =
            user.username;

        document.getElementById("user-detail-content").innerHTML = `
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-body">
                    <h5 class="mb-4">User Information</h5>

                    <div class="row g-3">
                        <div class="col-md-6">
                            <strong>Username</strong>
                            <p>${user.username}</p>
                        </div>

                        <div class="col-md-6">
                            <strong>Email</strong>
                            <p>${user.email || "-"}</p>
                        </div>

                        <div class="col-md-6">
                            <strong>First Name</strong>
                            <p>${user.first_name || "-"}</p>
                        </div>

                        <div class="col-md-6">
                            <strong>Last Name</strong>
                            <p>${user.last_name || "-"}</p>
                        </div>

                        <div class="col-md-6">
                            <strong>Referral Code</strong>
                            <p>${user.referral_code || "-"}</p>
                        </div>

                        <div class="col-md-6">
                            <strong>User ID</strong>
                            <p>${user.id}</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card shadow-sm border-0">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="mb-0">Referral Tree</h5>

                        <input
                            type="text"
                            id="referral-tree-search"
                            class="form-control"
                            style="max-width: 250px;"
                            placeholder="Search username..."
                            oninput="searchReferralTree()"
                        >
                    </div>

                    <div id="referral-tree">
                        ${buildReferralTree(tree)}
                    </div>
                </div>
            </div>
        `;

    } catch (error) {
        console.error("User detail loading error:", error);
    }
}


function buildReferralTree(node) {
    if (!node) {
        return `
            <p class="text-muted text-center">
                No referral members found.
            </p>
        `;
    }

    return `
        <div class="text-center mb-3">

            <div
                class="referral-node d-inline-block border rounded p-3 shadow-sm bg-white"
                data-search="${node.username.toLowerCase()}"
            >
                <strong>${node.username}</strong>
                <br>
                <small class="text-muted">
                    ${node.referral_code || ""}
                </small>
            </div>

            ${
                node.left || node.right
                    ? `
                        <div class="row mt-3">

                            <div class="col-6">
                                ${
                                    node.left
                                        ? buildReferralTree(node.left)
                                        : ""
                                }
                            </div>

                            <div class="col-6">
                                ${
                                    node.right
                                        ? buildReferralTree(node.right)
                                        : ""
                                }
                            </div>

                        </div>
                    `
                    : ""
            }

        </div>
    `;
}


function searchReferralTree() {
    const searchInput =
        document.getElementById("referral-tree-search");

    const searchTerm =
        searchInput.value.trim().toLowerCase();

    const nodes =
        document.querySelectorAll("#referral-tree .referral-node");

    nodes.forEach(node => {
        const username = node.dataset.search;

        if (!searchTerm) {
            node.classList.remove("border-primary", "border-3");
            return;
        }

        if (username.includes(searchTerm)) {
            node.classList.add("border-primary", "border-3");
        } else {
            node.classList.remove("border-primary", "border-3");
        }
    });
}