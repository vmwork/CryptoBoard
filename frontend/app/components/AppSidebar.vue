<script setup lang="ts">
import {
    IconListTree,
    IconChartBar,
    IconDashboard,
    IconDatabase,
    IconFileAi,
    IconDeviceAnalytics,
    IconNfc,
    IconHelp,
    IconBrandBinance,
    IconBrandMessenger,
    IconCashRegister,
    IconSearch,
    IconSettings,
    IconUsers,
    IconMail,
} from "@tabler/icons-vue"

import NavDocuments from "@/components/NavDocuments.vue"
import NavMain from "@/components/NavMain.vue"
import NavSecondary from "@/components/NavSecondary.vue"
import NavUser from "@/components/NavUser.vue"
import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"

const data = {
    user: {
        name: "shadcn",
        email: "m@example.com",
        avatar: "/avatars/shadcn.jpg",
    },
    navMain: [
        {
            title: "Analytics",
            url: "#",
            icon: IconDeviceAnalytics,
        },
        {
            title: "Messages",
            url: "#",
            icon: IconMail,
            iconAfter: IconBrandMessenger,
        },
        {
            title: "Classifieds",
            url: "#",
            icon: IconListTree,
        },
        {
            title: "Transactions",
            url: "#",
            icon: IconCashRegister,
        },
        {
            title: "My NFTs",
            url: "#",
            icon: IconNfc,
        },
    ],

    navSecondary: [
        {
            title: "Settings",
            url: "#",
            icon: IconSettings,
        },
        {
            title: "Get Help",
            url: "#",
            icon: IconHelp,
        },
        {
            title: "Search",
            url: "#",
            icon: IconSearch,
        },
    ],
    documents: [
        {
            name: "Data Library",
            url: "#",
            icon: IconDatabase,
        },
    ],
}
</script>

<template>
    <Sidebar collapsible="offcanvas">
        <SidebarHeader>
            <SidebarMenu>
                <SidebarMenuItem>
                    <SidebarMenuButton as-child class="data-[slot=sidebar-menu-button]:!p-1.5">
                        <a href="#">
                            <IconBrandBinance class="!size-5" />
                            <span class="text-base font-semibold">CryptoBoard</span>
                        </a>
                    </SidebarMenuButton>
                </SidebarMenuItem>
            </SidebarMenu>
        </SidebarHeader>
        <SidebarContent>
            <NavMain :items="data.navMain" />
            <NavDocuments :items="data.documents" />
            <NavSecondary :items="data.navSecondary" class="mt-auto" />
        </SidebarContent>
        <SidebarFooter>
            <NavUser :user="data.user" />
        </SidebarFooter>
    </Sidebar>
</template>
